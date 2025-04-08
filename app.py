import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Vexa – Visibility-as-a-Service", layout="wide")

# Load logo
logo_path = os.path.join("assets", "vexa_logo.png")

col1, col2 = st.columns([1, 8])
with col1:
    if os.path.exists(logo_path):
        st.image(logo_path, width=80)
    else:
        st.warning("Logo not found in /assets")
with col2:
    st.markdown("## Vexa – Visibility-as-a-Service for AI")
    st.markdown("*Bringing sponsored visibility into AI-generated content.*")

# Top navigation menu
st.markdown("""
<style>
.navbar {
    display: flex;
    gap: 2rem;
    font-size: 18px;
    margin-top: 10px;
    margin-bottom: 25px;
}
.navbar a {
    text-decoration: none;
    font-weight: bold;
    color: #1e1e2f;
}
</style>
<div class="navbar">
    <a href='/?page=home'>Home</a>
    <a href='/?page=how'>How it Works</a>
    <a href='/?page=submit'>Submit Content</a>
    <a href='/?page=partners'>Partners</a>
</div>
""", unsafe_allow_html=True)

# Get query params using updated method
query_params = st.query_params
page = query_params.get("page", "home")

# Page routing
if page == "home":
    st.markdown("### Welcome to Vexa")
    st.write("Vexa is your gateway to visibility inside LLM responses. It's not about ads — it's about relevance.")
    st.info("Use the menu above to explore the platform.")
elif page == "how":
    st.markdown("### How Vexa Works")
    st.write("""
1. Sponsor submits content.
2. Vexa transforms it into AI-friendly embeddings.
3. Content is stored and matched by context.
4. AI apps query Vexa to enrich their answers with relevant, sponsor-aligned responses.
    """)
elif page == "submit":
    st.markdown("### Submit Your Sponsored Content")
    with st.form("sponsor_form"):
        company = st.text_input("Company Name")
        email = st.text_input("Email")
        title = st.text_input("Content Title")
        content = st.text_area("Content Body")
        tags = st.text_input("Tags (comma-separated)")
        url = st.text_input("Website URL")
        language = st.selectbox("Language", ["English", "Spanish", "Other"])
        submit = st.form_submit_button("Submit")

        if submit:
            payload = {
                "company_name": company,
                "email": email,
                "content_title": title,
                "content_body": content,
                "tags": tags,
                "url": url,
                "language": language
            }
            try:
                r = st.requests.post("https://api.vexa.yourdomain.com/submit_content", json=payload)
                if r.status_code == 200:
                    st.success("Submission successful.")
                else:
                    st.error("Error submitting. Please try again.")
            except Exception as e:
                st.error(f"Connection error: {e}")
elif page == "partners":
    st.markdown("### Our Integration Partners")
    st.markdown("""
Vexa integrates with forward-thinking AI platforms:

- Forefront AI – Custom GPTs
- DeepInfra – Open model inference APIs
- Wisdolia – Smart summarization
- Sidekick – B2B workflow AI

Interested in becoming a partner? Reach out to us.
    """)
