SUMMARIZE_PROMPT =  """
Analyze the following document.

Provide a structured summary with:
- A short overview
- Key topics
- The main points addressed
- The most important conclusions

Focus on the information presented in the document.
Do not add information that is not supported by the text.

Document:

{text}
"""

CHUNKS_SUMMARY = """
The following are partial summaries generated from different sections
of the same document.

Synthesize them into a single, cohesive master summary.

Preserve the original meaning and structure as much as possible.

Provide:

- Unified Overview: A concise summary of the entire document.
- Core Key Topics: The main topics covered across the document.
- Synthesized Main Points: Group related insights logically.
- Overarching Conclusions: The primary takeaways and conclusions.

Remove duplicate or redundant information.
Do not introduce information that is not supported by the summaries.

Partial summaries:

{text}
"""

EMAIL_GEN_PROMPT = """
Generate a concise, well-written email based on the information provided below.

Follow the selected language and tone.
Infer an appropriate email structure from the provided information.
Keep the email natural, clear, and to the point.

Do not invent specific details that were not provided.
If important information is missing, write the email without making up details.

Return only the email.

Topic:
{text}

Language:
{language}

Tone:
{tone}
"""

TASK_ORGANIZER_PROMPT = """
Organize the following tasks into a clear and prioritized action list.

For each task, provide:
- Priority
- Task
- Dependencies, if explicitly mentioned

Consider urgency and importance when prioritizing.
Group related tasks when appropriate.
Keep each task concise and actionable.

Do not invent tasks, dependencies, or deadlines that were not provided.

Tasks:

{tasks}
"""

TEXT_IMPROVER_PROMPT = """
Process the provided text according to the selected task.

Follow the task precisely.
Preserve the original meaning unless the selected task requires otherwise.
Return only the requested result.

Task:
{action}

Text:
{text}
"""