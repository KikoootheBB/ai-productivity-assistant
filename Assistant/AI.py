from openai import OpenAI
from dotenv import load_dotenv
from assistant.prompts import pdf_prompt
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def summarize_text(text):
    prompt = f"""pdf_
        Summarize the following document.

        Provide:
        - A short overview
        - The main points
        - The most important conclusions

        Document:

        {text}
        """
    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text

def generate_email(text):
    prompt = f"""
        Generate a concise, well-written email from the subject provided below. Use the selected language and tone, and infer appropriate wording and structure from the subject.
        Keep it natural, professional, and to the point.

        Subject: {text}

        Language: [language]

        Tone: [tone]
        """
    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text

def organize_tasks(text):
    prompt = f"""
        Organize these tasks into a clear, prioritized action list.
        Group related tasks, identify dependencies, and order them by urgency and importance. 
        Keep each task concise and actionable.

        Tasks:

        {text}
        """
    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text

def text_improve(text):
    prompt = f"""
        Process the provided text according to the selected task.
        Follow the given task precisely, preserve the original meaning, and return only the requested result.

        Task: [task — e.g. summarize, proofread, rewrite, translate]

        Text: {text}

        """
    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text