import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

st.title("AI Productivity Assistant")

if api_key:
    st.success("API key loaded successfully")
    st.write(f"Key starts with: {api_key[:7]}...")
else:
    st.error("API key not found")