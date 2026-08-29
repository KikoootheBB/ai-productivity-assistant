from openai import OpenAI
from dotenv import load_dotenv
from .prompts import SUMMARIZE_PROMPT, EMAIL_GEN_PROMPT, TASK_ORGANIZER_PROMPT, TEXT_IMPROVER_PROMPT
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def summarize_text(text):
    prompt = SUMMARIZE_PROMPT.format(
        text=text
    )
    
    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text

def generate_email(text, lang, tone):
    prompt = EMAIL_GEN_PROMPT.format(
        text=text,
        lang=lang,
        tpne=tone
    )
    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text

def organize_tasks(tasks):
    prompt = TASK_ORGANIZER_PROMPT.format(
        tasks=tasks
    )

    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text

def text_improve(text, task):
    prompt = TEXT_IMPROVER_PROMPT.format(
        text=text,
        task=task
    )

    response = client.responses.create(model="gpt-5-nano", input=prompt)

    return response.output_text