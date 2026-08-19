from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def summarize_text(text):
    prompt = f"""
        Summarize the following document.

        Provide:
        - A short overview
        - The main points
        - The most important conclusions

        Document:

        {text}
        """
    response = client.responses.create(model="gpt-5.6", input=prompt)

    return response.output_text