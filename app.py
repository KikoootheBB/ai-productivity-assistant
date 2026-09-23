import streamlit as st
from assistant.pdf import PDFError, extract_text, split_text
from assistant.AI import (
    AIError,
    summarize_text, 
    summarize_chunks, 
    generate_email, 
    organize_tasks, 
    text_improve
)

# Page configuration
st.set_page_config(
    page_title="AI Productivity Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

def go_to_pdf():
    st.session_state.selected_page = "📄 PDF Summarizer"

def go_to_email():
    st.session_state.selected_page =  "✉️ Email Generator"

def go_to_task():
    st.session_state.selected_page = "✅ Task Organizer"

def go_to_text():
    st.session_state.selected_page = "✍️ Text Improver"

# Sidebar
with st.sidebar:
    st.title("🤖 AI Assistant")
    st.caption("Your personal productivity assistant")

    st.divider()

    page = st.radio(
        "Tools",
        [
            "🏠 Home",
            "📄 PDF Summarizer",
            "✉️ Email Generator",
            "✅ Task Organizer",
            "✍️ Text Improver",
        ],
        key="selected_page"
    )

    st.divider()

    st.caption("AI Productivity Assistant")
    st.caption("Built with Python + Streamlit")

# HOME
if page == "🏠 Home":

    st.markdown(
    """
    <style>
        .main-title {
            text-align: center;
        }

        .main-subtitle {
            text-align: center;
        }

        .main-description {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
    )   

    st.markdown(
        '<h1 class="main-title">AI Productivity Assistant</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<h3 class="main-subtitle">Your personal AI-powered productivity toolkit.</h3>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="main-description">Use AI to summarize documents, generate emails, organize tasks and improve your writing.</p>',
        unsafe_allow_html=True
    )

    st.divider()

    # Two by two grid for the tools
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>📄 PDF Summarizer</h3>
                <p>Upload a PDF and generate a concise summary.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Summarize PDF", 
            use_container_width=True, 
            on_click = go_to_pdf
        ):
            pass

    with col2:
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>✉️ Email Generator</h3>
                <p>Generate professional emails using AI.</p>
            </div>
            """,
            unsafe_allow_html=True
        ) 

        if st.button(
            "Generate Email", 
            use_container_width=True, 
            on_click = go_to_email
        ):
            pass

    col3, col4 = st.columns(2)

    with col3:
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>✅ Task Organizer</h3>
                <p>Organize and prioritize your tasks.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "Organize Tasks", 
            use_container_width=True, 
            on_click = go_to_task
        ):
            pass
            
    with col4:
        st.markdown(
            """
            <div style="text-align: center;">
                <h3>✍️ Text Improver</h3>
                <p>Edit and clean your texts.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
           "Improve Text", 
            use_container_width=True, 
            on_click = go_to_text
        ):
            pass

    st.divider()

    st.subheader("How it works")

    step1, step2, step3 = st.columns(3)

    with step1:
        st.markdown("### 1️⃣ Input")
        st.write("Provide your document, text or task list.")

    with step2:
        st.markdown("### 2️⃣ AI Processing")
        st.write("The AI analyzes your input.")

    with step3:
        st.markdown("### 3️⃣ Result")
        st.write("Receive a useful, structured result.")

# PDF SUMMARIZER
elif page == "📄 PDF Summarizer":

    st.title("📄 PDF Summarizer")

    st.write(
        "Upload a PDF and the AI will generate a summary."
    )

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"],
        key="pdf_upload"
    )

    if uploaded_file:
        st.success(f"File uploaded: {uploaded_file.name}")

        if st.button(
            "Summarize PDF",
            type="primary",
            use_container_width=True
        ):
            try:
                with st.spinner("Reading PDF..."):
                    pdf_text, full_length = extract_text(uploaded_file)

                st.caption(f"PDF text length: {full_length:,} characters")

            except PDFError:
                st.error(
                    "⚠️ Unable to read this PDF.\n\n"
                    "Please make sure the file is a valid PDF containing readable text."
                )

            else:
                try:    
                    with st.spinner("Analyzing document..."):
                        if full_length <= 20000:
                            summary = summarize_text(pdf_text)
                        else:
                            chunks = split_text(pdf_text)
                            st.caption(f"Large document detected. Processing {len(chunks)} chunks...")
                            summary = summarize_chunks(chunks)

                    st.write(summary)

                except AIError:
                    st.error(
                        "⚠️ Unable to generate the summarized text.\n\n"
                    "Please check your API configuration and try again."
                    )

# EMAIL GENERATOR
elif page == "✉️ Email Generator":

    st.title("✉️ Email Generator")

    st.write(
        "Generate a professional email using AI."
    )

    topic = st.text_area(
        "What should the email be about?",
        placeholder="Example: Requesting vacation days...",
        key= "email_input"
    )

    tone = st.selectbox(
        "Choose the tone",
        [
            "Professional",
            "Friendly",
            "Formal",
            "Casual"
        ]
    )

    language = st.selectbox(
        "Language",
        [
            "English",
            "Portuguese",
            "Spanish",
            "French"
        ]
    )

    if st.button(
        "Generate Email",
        type="primary",
        use_container_width=True
    ):
        if not topic or not any(char.isalnum() for char in topic):
            st.warning("Please describe what the email should be about.")
        else:
            try:
                with st.spinner("Generating email..."):
                    proper_email = generate_email(topic, language, tone)

                st.text_area(
                    "Generated email",
                    proper_email,
                    height=300
                )

            except AIError:
                st.error(
                    "⚠️ Unable to generate email as requested.\n\n"
                    "Please check your API configuration and try again."
                )
                
# TASK ORGANIZER
elif page == "✅ Task Organizer":

    st.title("✅ Task Organizer")

    st.write(
        "Enter your tasks and let AI organize and prioritize them."
    )

    tasks = st.text_area(
        "Your tasks",
        placeholder=(
            "Example:\n"
            "Send CV\n"
            "Buy groceries\n"
            "Study Python\n"
            "Reply to emails"
        ),
        height=200,
        key= "todo_input"
    )

    if st.button(
        "Organize Tasks",
        type="primary",
        use_container_width=True
    ):
        if not tasks or not any(char.isalnum() for char in tasks):
            st.warning("Please enter at least one task.")
        else:
            try:
                with st.spinner("Organizing tasks..."):
                    organized = organize_tasks(tasks)

                st.subheader("Organized tasks:")
                st.write(organized)

            except AIError:
                st.error(
                    "⚠️ Unable to generate the organized tasks.\n\n"
                    "Please check your API configuration and try again."
                )

# TEXT IMPROVER
elif page == "✍️ Text Improver":

    st.title("✍️ Text Improver")

    st.write(
        "Improve, rewrite or correct your text using AI."
    )

    text = st.text_area(
        "Enter your text",
        placeholder="Paste your text here...",
        height=250,
        key="text_improver_input"
    )

    action = st.selectbox(
        "What would you like to do?",
        [
            "Improve writing",
            "Correct grammar",
            "Make it more professional",
            "Make it shorter",
            "Make it longer"
        ]
    )

    if st.button(
        "Improve Text",
        type="primary",
        use_container_width=True
    ):
        if not text or not any(char.isalnum() for char in text):
            st.warning("Please enter some meaningful text.")
        else:
            try:
                with st.spinner("Improving text..."):    
                    final_text = text_improve(text, action)

                st.text_area(
                    "Improved text",
                    final_text,
                    height=250
                )

            except AIError:
                st.error(
                    "⚠️ Unable to generate improved text.\n\n"
                    "Please check your API configuration and try again."
                )