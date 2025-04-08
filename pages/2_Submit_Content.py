import streamlit as st
import requests

st.title("Submit Your Sponsored Content")

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
            r = requests.post("https://api.vexa.yourdomain.com/submit_content", json=payload)
            if r.status_code == 200:
                st.success("✅ Submission successful!")
            else:
                st.error("⚠️ Error submitting. Please try again.")
        except Exception as e:
            st.error(f"⚠️ Failed to connect: {e}")