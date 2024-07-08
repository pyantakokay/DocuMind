![Logo](V3-Logo.png)

#  ~ DocuMind ~
Introducing DocuMind, a powerful tool that allows you to generate personalized summaries of PDF documents. Leveraging the latest advancements in natural language processing and machine learning, this tool empowers you to tailor the summarization process to your specific needs, ensuring you get the most relevant and insightful information from your source material.

## <div align="center">Demo</div>

### Overview

### Main Look
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo1.png)

### PDF uploaded successfully
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo2.png)

### Entered prompt and summarized PDF using map_reduce w/ default values
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo3.png)

### Summarized PDF using stuff w/ default values
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo4.png)


### Summarized PDF using refine w/ default values
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo5.png)


### ZIP file uploaded successfully (5 PDF files)
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo6.png)


### Summarized ZIP using map_reduce w/ default values
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo7.png)

### Summarized ZIP using stuff w/ default values
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo8.png)

### Summarized ZIP using refine w/ default values
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo9.png)

### Interactive Text Chunk Visualizer (Debug Chunk Size)
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo10.png)

### Text Splitter Visualizer
![Image](https://github.com/pyantakokay/DocuMind/blob/main/Demo%20Screenshots/Demo11.png)

## Badges
  ![Brave](https://img.shields.io/badge/Brave-FB542B?style=for-the-badge&logo=Brave&logoColor=white)
  ![Replit](https://img.shields.io/badge/Replit-DD1200?style=for-the-badge&logo=Replit&logoColor=white)
  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-0.89.0-brightgreen)


---

# Features

- **Flexible Chain Types:** The tool offers a choice of different summarization chains allowing users to experiment and find the most suitable approach for their requirements.

- **Adjustable Parameters:** Users have control over the amount of detail and granularity in the summaries that are generated.

- **Tailored Prompts:** Users can input their own prompts to guide the summarization process, ensuring the generated summaries are tailored to their specific needs.

- **Interactive Chunk Visualization:** Visualize text chunks with color-coded highlights.

---

# API Reference

<div align="center">

| Requirements          | Type            | Description                                                                                                  |
|-----------------------|-----------------|--------------------------------------------------------------------------------------------------------------|
| `openai`              | Python Package  | **Required**. A client library for accessing the OpenAI API, enabling the use of various AI models.          |
| `langchain`           | Python Package  | **Required**. A framework for building applications using large language models.                              |
| `langchain-community` | Python Package  | **Required**. Community-driven extensions and enhancements for LangChain, including additional models.        |
| `langchain-openai`    | Python Package  | **Required**. Integration module for using OpenAI's models within LangChain.                                  |
| `pymupdf`             | Python Package  | **Required**. A library for reading and manipulating PDF files in Python.                                      |
| `streamlit`           | Python Package  | **Required**. An open-source app framework for creating and sharing data apps.                                |

</div>

<div align="center">

| Parameter              | Type     | Description                           |
|------------------------|----------|---------------------------------------|
| `OPENAI_SECRET_KEY`    | `string` | **Required**. Your API key.           |

</div>

## Installation

#### Run this in Shell:
```bash
pip install -r requirements.txt
```
# Usage
```python
streamlit run main.py
```

# Author
[@pyantakokay](https://github.com/pyantakokay)

## Acknowledgements

I would like to thank AI Nusantara (AIN) for offering the AI in Application Design course for free, which significantly contributed to the knowledge and skills required to complete this project.


I would also like to thank the following platforms for their contributions and support:

- Streamlit: For creating an easy-to-use framework for building data applications.
- Replit: For providing a collaborative coding environment that facilitated the development of this project.
- OpenAI: For providing powerful AI models and the OpenAI API.
- LangChain: For offering a comprehensive framework for working with large language models.
