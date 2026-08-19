import streamlit as st
from assistant.pdf import extract_text

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

    # # Simple titles auto left
    # st.title("AI Productivity Assistant")
    # st.subheader("Your personal AI-powered productivity toolkit.")

    # st.write(
    #     "Use AI to summarize documents, generate emails, "
    #     "organize tasks and improve your writing."
    # )

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

    # Three columns for the main tools
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📄 PDF Summarizer")
        st.write(
            "Upload a PDF and generate a concise summary."
        )

        if st.button(
            "Summarize PDF", 
            use_container_width=True, 
            on_click = go_to_pdf
        ):
            pass

    with col2:
        st.subheader("✉️ Email Generator")
        st.write(
            "Generate professional emails using AI."
        )

        if st.button("Generate Email", use_container_width=True):
            st.info("Email Generator coming soon.")

    with col3:
        st.subheader("✅ Task Organizer")
        st.write(
            "Organize and prioritize your tasks."
        )

        if st.button("Organize Tasks", use_container_width=True):
            st.info("Task Organizer coming soon.")

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
        key="pdf_update"
    )

    if uploaded_file:
        st.success(f"File uploaded: {uploaded_file.name}")

        if st.button(
            "Summarize PDF",
            type="primary",
            use_container_width=True
        ):
            result = extract_text(uploaded_file)
            st.write(result)

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
        if not topic:
            st.warning("Please describe what the email should be about.")
        else:
            st.info("AI email generation will be added next.")

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
        if not tasks:
            st.warning("Please enter at least one task.")
        else:
            st.info("AI task organization will be added next.")

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
        if not text:
            st.warning("Please enter some text.")
        else:
            st.info("AI text improvement will be added next.")