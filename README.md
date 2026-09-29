# AI Productivity Assistant

A Streamlit-based AI productivity assistant that provides a collection of practical tools powered by the OpenAI API.

The project was built to explore practical applications of Large Language Models (LLMs), prompt engineering, API integration, document processing, and modular Python application design.

## Features

### PDF Summarizer

- Extracts text from uploaded PDF documents.
- Detects large documents based on extracted text length.
- Splits large documents into token-based chunks using `tiktoken`.
- Generates summaries for individual chunks.
- Synthesizes the chunk summaries into a single structured summary.
- Handles PDFs with no readable text.

### Email Generator

- Generates emails from a short description.
- Supports multiple languages.
- Supports different tones, including:
  - Professional
  - Friendly
  - Formal
  - Casual

### Task Organizer

- Converts an unstructured list of tasks into a prioritized action list.
- Considers urgency and importance.
- Groups related tasks when appropriate.
- Identifies dependencies when they are explicitly provided.

### Text Improver

Supports several text transformation tasks:

- Improve writing
- Correct grammar
- Make it more professional
- Make it shorter
- Make it longer

## Architecture

The project uses a modular structure where each component has a specific responsibility.

AI-Productivity-Assistant/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── assistant/
    ├── ai.py
    ├── pdf.py
    └── prompts.py

## Component responsibilities

app.py
    Handles the Streamlit interface, user input, navigation, validation, loading states, and error messages.

assistant/ai.py
    Handles communication with the OpenAI API and contains the application's AI-related functions.

assistant/pdf.py
    Handles PDF text extraction and token-based document chunking.

assistant/prompts.py
    Contains the prompts used by the different AI tools.

## Technologies

Python
Streamlit
OpenAI API
pypdf
tiktoken
python-dotenv
Git / GitHub

## Instalation

1. Clone the repository

git clone https://github.com/KikoootheBB/ai-productivity-assistant.git
cd ai-productivity-assistant

2. Create a virtual environment

python -m venv .venv

Activate it on Windows:
.venv\Scripts\Activate.ps1

3. Install dependencies

pip install -r requirements.txt

4. Configure the API key

Create a .env file in the project root with the text:

OPENAI_API_KEY= *Your_api_key_here*
The .env file should not be committed to Git.

5. Run the application

streamlit run app.py

The application should then open in your browser.

## Limitations

- The application requires an OpenAI API key.
- API usage may incur costs depending on the configured OpenAI account.
- PDF summarization depends on the ability to extract readable text from the document.
- Image-only or scanned PDFs without an extractable text layer are not currently processed with OCR.
- Large documents require multiple AI requests and therefore may use more API tokens.
- The application currently uses a fixed model configuration.