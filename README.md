![Logo](V3-Logo.png)

#  ~ DocuMind ~
Introducing DocuMind, a powerful tool that allows you to generate personalized summaries of PDF documents. Leveraging the latest advancements in natural language processing and machine learning, this tool empowers you to tailor the summarization process to your specific needs, ensuring you get the most relevant and insightful information from your source material.

## <div align="center">Demo</div>

### Overview
![Image](Demo Screenshots/Demo1.png)
![Image](Demo Screenshots/Demo2.png)
![Image](Demo Screenshots/Demo3.png)
![Image](Demo Screenshots/Demo4.png)
![Image](Demo Screenshots/Demo5.png)
![Image](Demo Screenshots/Demo6.png)
![Image](Demo Screenshots/Demo7.png)
![Image](Demo Screenshots/Demo8.png)
![Image](Demo Screenshots/Demo9.png)
![Image](Demo Screenshots/Demo10.png)
![Image](Demo Screenshots/Demo11.png)

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
