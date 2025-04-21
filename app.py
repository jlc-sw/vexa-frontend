# app.py  (landing page)
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="AI‑Powered Advertising",
    layout="wide",          # or "centered" – either way the sidebar stays
    initial_sidebar_state="expanded"
)

# ---------------- sidebar  ----------------
with st.sidebar:
    st.image("assets/vexa_logo.png", width=160)
    page = st.radio("Navigate", ["Home", "Dashboard", "Settings"])

# --------------- main area ----------------
if page == "Home":
    # 1. Read the HTML you showed me earlier
    html = Path("static/ai_landing.html").read_text(encoding="utf‑8")

    # 2. Show it in an iframe
    components.html(
        html,
        height=3300,       # tweak until the whole page fits, or enable scrolling
        scrolling=True
    )

elif page == "Dashboard":
    st.header("📊  Interactive dashboard")
    # … rest of your Streamlit widgets …

elif page == "Settings":
    st.header("⚙️  Settings")
    # …
