from openai import OpenAI
from dotenv import load_dotenv
from .prompts import SUMMARIZE_PROMPT, CHUNKS_SUMMARY, EMAIL_GEN_PROMPT, TASK_ORGANIZER_PROMPT, TEXT_IMPROVER_PROMPT
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

def summarize_chunks(chunks):
    summaries = []

    for chunk in chunks:
        summary = summarize_text(chunk)
        summaries.append(summary)

    final_summary = chunks_final_summary(summaries)

    return final_summary    

def chunks_final_summary(summaries):
    prompt = CHUNKS_SUMMARY.format(
        text="\n\n".join(summaries)
    )
        
    response = client.responses.create(model="gpt-5-nano", input=prompt)
    
    return response.output_text

def generate_email(text, language, tone):
    prompt = EMAIL_GEN_PROMPT.format(
        text=text,
        language=language,
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