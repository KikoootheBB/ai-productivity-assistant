SUMMARIZE_PROMPT = """
        Summarize the following document.

        Provide:
        - A short overview
        - The main points
        - The most important conclusions

        Document:

        {text}
        """
 
EMAIL_GEN_PROMPT = """
        Generate a concise, well-written email from the subject provided below. Use the selected language and tone, and infer appropriate wording and structure from the subject.
        Keep it natural, professional, and to the point.

        Subject: 
        {text}

        Language: 
        {lang}

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