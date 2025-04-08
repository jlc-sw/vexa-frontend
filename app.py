import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Vexa – Visibility-as-a-Service", layout="centered")

# Safe path loading
logo_path = os.path.join("assets", "vexa_logo.png")

# Check if the file exists
if os.path.exists(logo_path):
    st.image(logo_path, width=150)
else:
    st.warning("⚠️ Logo not found — make sure vexa_logo.png is in /assets folder.")

st.title("Vexa – Visibility-as-a-Service for AI")

st.markdown("""
Welcome to **Vexa**, the first platform that helps businesses gain visibility *inside* AI-generated answers.

> Vexa bridges AI platforms and sponsored content in a natural, context-aware way.

**🔗 Use the sidebar to:**
- Understand how it works
- Submit your content
- Explore AI platforms we integrate with
""")
