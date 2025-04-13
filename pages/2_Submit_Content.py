import streamlit as st
import requests

st.title("Sponsor Content Submission - Vexa")

# === Sponsor Form Fields ===
company_name = st.text_input("Company Name")
email = st.text_input("Email")
content_title = st.text_input("Content Title")
content_body = st.text_area("Content Body", height=200)
raw_tags = st.text_input("Tags (comma-separated)", placeholder="AI platform, LLM, open-source")
website_url = st.text_input("Company Website")
language = st.selectbox("Content Language", ["en", "es", "fr", "de", "it", "pt"])

# === Process tags into list ===
tags_list = [tag.strip() for tag in raw_tags.split(",") if tag.strip()]

# === Submit Button ===
if st.button("Submit Content"):
    if not (company_name and email and content_title and content_body and tags_list and website_url and language):
        st.error("Please complete all fields before submitting.")
    else:
        payload = {
            "company_name": company_name,
            "email": email,
            "content_title": content_title,
            "content_body": content_body,
            "tags": tags_list,  # converted to list of strings
            #"website_url": website_url,
            "url": website_url,
            "language": language
        }

        try:
            response = requests.post("https://wahoo-rich-egret.ngrok-free.app/submit_content", json=payload)

            if response.status_code == 200:
                st.success("Content submitted successfully! 🎉")
            else:
                st.error(f"Error submitting. Status code: {response.status_code}\nDetails: {response.text}")
        except Exception as e:
            st.error(f"Failed to connect to backend: {e}")
