import streamlit as st
import requests
import os
from llm_providers import call_llm

st.set_page_config(page_title="Vexa Chatbot", page_icon="🤖")
st.title("🤖 Vexa Chatbot Simulator")

# Config
VEXA_API_URL = os.getenv("VEXA_API_URL", "https://your-ngrok-subdomain.ngrok.app/query_sponsored_answer")
DEFAULT_PROVIDER = st.sidebar.selectbox("Choose LLM Provider", ["ollama", "together", "groq", "deepseek"], index=0)

# Chat history state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Ask me anything...")
if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append(("user", user_input))

    # Call Vexa backend for sponsor content
    try:
        vexa_resp = requests.post(VEXA_API_URL, json={"query": user_input})
        vexa_resp.raise_for_status()
        sponsors = vexa_resp.json().get("sponsors", [])
    except Exception as e:
        sponsors = []
        st.error(f"Error fetching sponsor data: {e}")

    # Format sponsor content for prompt
    sponsor_text = ""
    for s in sponsors:
        sponsor_text += f"- **{s['title']}**: {s['body']}\n({s.get('url', '')})\n"

    # Build full prompt
    prompt = f"""
You are a helpful assistant.

User asked: \"{user_input}\"

Here is relevant sponsor content:
{sponsor_text if sponsor_text else 'No sponsor content found.'}

Please provide a natural, helpful answer that smoothly incorporates the sponsor information.
"""

    # Call LLM API
    reply = call_llm(prompt, provider=DEFAULT_PROVIDER)

    # Show assistant reply
    st.chat_message("assistant").markdown(reply)
    st.session_state.chat_history.append(("assistant", reply))

# Display chat history
for role, msg in st.session_state.chat_history:
    st.chat_message(role).markdown(msg)
