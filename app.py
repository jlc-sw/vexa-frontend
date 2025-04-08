import streamlit as st
from PIL import Image

st.set_page_config(page_title="Vexa – Visibility-as-a-Service", layout="centered")

st.image("assets/vexa_logo.png", width=150)
st.title("Vexa – Visibility-as-a-Service for AI")

st.markdown("""
Welcome to **Vexa**, the first platform that helps businesses gain visibility *inside* AI-generated answers.

> Vexa bridges AI platforms and sponsored content in a natural, context-aware way.

**🔗 Use the sidebar to:**
- Understand how it works
- Submit your content
- Explore AI platforms we integrate with
""")