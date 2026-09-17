SUMMARIZE_PROMPT = """
        Analize the following document.

       Then provide a structured summary with:
        - A short overview
        - The Key topics
        - The main points addressed
        - The most important conclusions

        Document:

        {text}
        """

CHUNKS_SUMMARY = """
        Take the following compilation of summaries and synthesize it
        into a single, cohesive master summary.

        Preserve the original structure and meaning as much as possible.

        Provide:

        - Unified Overview: A concise summary of the entire document.
        - Core Key Topics: The main topics covered across the document.
        - Synthesized Main Points: Group related insights together logically.
        - Overarching Conclusions: The primary takeaways and conclusions.

        Remove duplicate or redundant information.

        Compilation:

        {text}
"""

EMAIL_GENERATOR_PROMPT = """
        Generate a concise, well-written email based on the information provided below.

        Follow the selected language and tone.
        Infer an appropriate email structure from the provided information.
        Keep the email natural, clear, and to the point.

        Return only the email.

        Topic:
        {text}

        Language:
        {language}

        Tone:
        {tone}
        """

TASK_ORGANIZER_PROMPT = """
        Organize these tasks into a clear, prioritized action list.
        Group related tasks, identify dependencies, and order them by urgency and importance. 
        Keep each task concise and actionable.

        Tasks:
        {tasks}
        """

TEXT_IMPROVER_PROMPT = """
        Process the provided text according to the selected task.

        Follow the given task precisely, preserve the original meaning, and return only the requested result.

        Task:
        {task}

        Text:
        {text}
        """