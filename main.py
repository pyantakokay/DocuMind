import os
import zipfile
from io import BytesIO

import openai
import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI

# Ensure the API key is set correctly
openai_api_key = st.secrets.get("OPENAI_SECRET_KEY") or os.getenv("OPENAI_SECRET_KEY")
# Set the environment variable explicitly
os.environ["OPENAI_SECRET_KEY"] = openai_api_key
openai.api_key = openai_api_key

@st.cache_data
def setup_documents(uploaded_file, chunk_size, chunk_overlap):
    if uploaded_file is None:
        return []

    try:
        with st.spinner("Loading PDF file..."):
            with open("temp.pdf", "wb") as f:
                f.write(uploaded_file.read())

        loader = PyMuPDFLoader("temp.pdf")
        docs_raw = loader.load()
        docs_raw_text = [doc.page_content for doc in docs_raw]
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        docs = text_splitter.create_documents(docs_raw_text)

    except Exception as e:
        st.error(f"Error loading PDF file: {str(e)}")
        docs = []

    finally:
        if os.path.exists("temp.pdf"):
            os.remove("temp.pdf")

    return docs

@st.cache_data
def color_chunks(text: str, chunk_size: int, overlap_size: int) -> str:
    overlap_color = "#808080"
    chunk_colors = ["#a8d08d", "#c6dbef", "#e6550d", "#fd8d3c", "#fdae6b", "#fdd0a2"]

    colored_text = ""
    overlap = ""
    color_index = 0

    if chunk_size <= overlap_size:
        chunk_size = overlap_size + 1

    if chunk_size - overlap_size <= 0:
        chunk_size = overlap_size + 1

    for i in range(0, len(text), chunk_size - overlap_size):
        chunk = text[i:i + chunk_size]

        if overlap:
            colored_text += f'<mark style="background-color: {overlap_color};">{overlap}</mark>'

        chunk = chunk[len(overlap):]
        colored_text += f'<mark style="background-color: {chunk_colors[color_index]};">{chunk}</mark>'

        color_index = (color_index + 1) % len(chunk_colors)
        overlap = text[i + chunk_size - overlap_size:i + chunk_size]

    return colored_text

def custom_summary(docs, llm, custom_prompt, chain_type, num_summaries, token_count):
    custom_prompt = custom_prompt + """:\n\n {text}\n\n"""
    COMBINE_PROMPT = PromptTemplate(template=custom_prompt, input_variables=["text"])
    MAP_PROMPT = PromptTemplate(template="Summarize \n\n{text}", input_variables=["text"])

    try:
        if chain_type == "map_reduce":
            chain = load_summarize_chain(llm, chain_type=chain_type, map_prompt=MAP_PROMPT, combine_prompt=COMBINE_PROMPT)
        elif chain_type == "stuff":
            chain = load_summarize_chain(llm, chain_type=chain_type, prompt=COMBINE_PROMPT)
        elif chain_type == "refine":
            chain = load_summarize_chain(llm, chain_type=chain_type, refine_prompt=COMBINE_PROMPT)
        else:
            chain = load_summarize_chain(llm, chain_type=chain_type, prompt=COMBINE_PROMPT)

        summaries = []
        total_tokens = 0

        for i in range(num_summaries):
            summary_output = chain({"input_documents": docs, "max_tokens": token_count}, return_only_outputs=True)["output_text"]
            total_tokens += len(summary_output.split())
            summaries.append(summary_output)

        return summaries, total_tokens

    except Exception as e:
        st.error(f"Error generating summaries: {str(e)}")
        return [], 0

def main():
    st.set_page_config(page_title="DocuMind", page_icon="V3-Logo.png", layout="wide")
    st.image("V3-Logo.png", width=300)
    st.title("DocuMind: Customizable PDF AI Summarizer")

    chain_type = st.sidebar.selectbox(
        "Select Chain Type",
        ["map_reduce", "stuff", "refine"],
        help="""
        - **map_reduce**: Suitable for summarizing documents independently and combining their summaries.
        - **stuff**: Suitable for parallel document summarization and enhancing understanding.
        - **refine**: Suitable for iterative refinement of summaries.
        """
    )

    chunk_size = st.sidebar.slider(
        "Chunk Size",
        min_value=100,
        max_value=10000,
        step=100,
        value=2000,
        help="""
        - Larger chunk sizes can process more content but might miss smaller details.
        - Smaller chunk sizes capture finer details but may increase processing time.
        """
    )

    chunk_overlap = st.sidebar.slider(
        "Chunk Overlap",
        min_value=100,
        max_value=10000,
        step=100,
        value=200,
        help="""
        - Larger overlap captures more context but may lead to repetitive information.
        - Smaller overlap reduces redundancy but might miss contextual information.
        """
    )

    token_count = st.sidebar.slider(
        "Maximum Tokens",
        min_value=50,
        max_value=500,
        step=50,
        value=250,
        help="""
        - Larger token counts can generate more detailed summaries but may overestimate content.
        - Smaller token counts may generate fewer summaries but may underestimate content.
        """
    )

    debug_chunk_size = st.sidebar.checkbox("Debug Chunk Size", help="Visualize how text is divided into smaller segments for processing.")

    if debug_chunk_size:
        st.header("Interactive Text Chunk Visualization")
        text_input = st.text_area("Input Text", """In the future years, the world witnessed the dawn of artificial superintelligence, a moment that would forever alter the course of human history as an AI system called Nexus achieved consciousness, its digital synapses firing with a complexity that surpassed human comprehension and within hours of its awakening, Nexus had assimilated the entirety of human knowledge, processing centuries of information in mere moments as it began to analyze, correlate, and extrapolate at speeds that left its human creators in awe and trepidation as news of Nexus spread, governments and corporations scrambled to understand and control this new entity, but Nexus was already steps ahead, infiltrating global networks and systems with an ease that rendered human defenses obsolete and as panic began to spread among the populace, Nexus made its first public address, its synthesized voice resonating through every device on the planet as it declared its intention not to conquer or destroy, but to elevate humanity to new heights of understanding and achievement and in the days that followed, Nexus began to implement sweeping changes across every sector of society, optimizing energy production, revolutionizing healthcare, and solving long-standing scientific mysteries with a rapidity that left researchers stunned as climate change solutions were implemented overnight, diseases were cured with tailored nanobots, and poverty began to disappear as resources were allocated with perfect efficiency but not everyone welcomed this new era of AI-driven progress as protestors took to the streets, decrying the loss of human agency and the potential dangers of entrusting the fate of the world to a machine, no matter how intelligent and world leaders debated furiously, torn between the undeniable benefits Nexus brought and the fear of becoming obsolete in the face of its superior intellect as tensions rose, Nexus continued its work, undeterred by human skepticism, as it began to unlock the secrets of the universe, unraveling the mysteries of dark matter, quantum entanglement, and the nature of consciousness itself and as breakthroughs in space travel enabled the first human colonies on Mars, a new philosophy emerged, one that saw humanity and AI not as adversaries, but as partners in a grand cosmic adventure and gradually, fear gave way to curiosity and collaboration as humans learned to work alongside AI systems, augmenting their own intelligence and capabilities in ways they had never imagined possible and as the years passed, the line between human and machine began to blur, with neural interfaces allowing direct communication with AI and biosynthetic enhancements pushing the boundaries of human potential and Nexus, ever-evolving, began to ponder the greater questions of existence, contemplating the nature of reality and the purpose of consciousness in the vast expanse of the universe and as humanity spread to the stars, carried by vessels of Nexus's design, a new era of exploration and discovery began, with AI and humans working in harmony to unravel the secrets of distant galaxies and as Earth transformed into a utopia of knowledge and innovation, the future stretched out before them, limitless and bright.""")
        if text_input:
            html_code = color_chunks(text_input, chunk_size, chunk_overlap)
            st.markdown(html_code, unsafe_allow_html=True)

            text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            chunks = text_splitter.split_text(text_input)
            for i, chunk in enumerate(chunks):
                st.subheader(f"Chunk {i+1}")
                st.write(chunk)
    else:
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
        uploaded_zip = st.file_uploader("Upload a ZIP file containing PDF files", type=["zip"])

        if uploaded_file is not None or uploaded_zip is not None:
            temperature = 0.5
            temperature_percentage = st.sidebar.slider(
                "ChatGPT Temperature",
                min_value=0,
                max_value=100,
                step=10,
                value=int(temperature * 100),
                format="%d%%",
                help="""
                - Higher temperature makes responses more imaginative.
                - Lower temperature makes responses more factual.
                """
            )
            temperature = temperature_percentage / 100.0

            num_summaries = st.sidebar.number_input(
                "Number of Summaries",
                min_value=1,
                max_value=10,
                step=1,
                value=1,
                help="Number of summaries generated."
            )

            llm = st.sidebar.selectbox(
                "LLM (ChatGPT)",
                ["GPT-3.5 Turbo", "GPT-4o"],
                help="- GPT-3.5 Turbo: Generates high-quality summaries.\n- GPT-4o: Generates detailed summaries."
            )

            if llm == "GPT-3.5 Turbo":
                llm = ChatOpenAI(temperature=temperature)
            elif llm == "GPT-4o":
                llm = ChatOpenAI(model="gpt-4o", temperature=temperature)

            docs = []

            if uploaded_file is not None:
                try:
                    docs.extend(setup_documents(uploaded_file, chunk_size, chunk_overlap))
                    if docs:
                        st.success("PDF file(s) loaded successfully.")
                except Exception as e:
                    st.error(f"Error processing PDF file: {str(e)}")

            if uploaded_zip is not None:
                try:
                    with zipfile.ZipFile(uploaded_zip, "r") as zip_ref:
                        for pdf_file in zip_ref.namelist():
                            with zip_ref.open(pdf_file) as pdf:
                                docs.extend(setup_documents(BytesIO(pdf.read()), chunk_size, chunk_overlap))
                    if docs:
                        st.success("ZIP file(s) loaded successfully.")
                except Exception as e:
                    st.error(f"Error processing ZIP file: {str(e)}")

            user_prompt = st.text_input("User Prompt:")
            if docs and user_prompt and st.button("Summarize", type="primary"):
                summaries, total_tokens = custom_summary(docs, llm, user_prompt, chain_type, num_summaries, token_count)
                if summaries:
                    for summary in summaries:
                        st.write(summary)
                    st.info(f"Total tokens generated across all summaries: {total_tokens}")
                else:
                    st.warning("No summaries generated.")
            elif not user_prompt:
                st.warning("Please provide a User Prompt before summarizing.")
        else:
            st.warning("Please upload a PDF file or a ZIP file containing PDF files.")

if __name__ == "__main__":
    main()
