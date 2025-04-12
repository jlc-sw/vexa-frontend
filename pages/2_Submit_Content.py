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

    # ISO language codes
    lang_map = {
        "English": "en",
        "Spanish": "es",
        "Other": "xx"
    }
    language_selection = st.selectbox("Language", list(lang_map.keys()))
    language_code = lang_map.get(language_selection, "xx")

    submit = st.form_submit_button("Submit")

    if submit:
        # Clean tags into list
        tag_list = [tag.strip() for tag in tags.split(",") if tag.strip()]

        # Validate all required fields
        if not all([company, email, title, content, tag_list, url, language_code]):
            st.warning("⚠️ Please fill out all fields before submitting.")
        else:
            payload = {
                "company_name": company,
                "email": email,
                "content_title": title,
                "content_body": content,
                "tags": tag_list,
                "url": url,
                "language": language_code
            }

            try:
                headers = {
                    "ngrok-skip-browser-warning": "true"
                }
                backend_url = "https://wahoo-rich-egret.ngrok-free.app/submit_content"
                r = requests.post(backend_url, json=payload, headers=headers)
                if r.status_code == 200:
                    st.success("✅ Submission successful!")
                else:
                    st.error(f"⚠️ Error submitting. Status code: {r.status_code}")
            except Exception as e:
                st.error(f"⚠️ Failed to connect: {e}")
