import requests
import os
import streamlit as st
import re
from together import Together

# Get the key from Streamlit's secrets storage
together_client = Together(api_key=st.secrets["TOGETHER_API_KEY"])

# Try Streamlit secrets first, then fallback to env var (for local dev)
try:
    #import streamlit as st
    TOGETHER_API_KEY = st.secrets["TOGETHER_API_KEY"]
except ImportError:
    TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")


#TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
#together_client = Together(api_key=TOGETHER_API_KEY)

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")

def call_llm(prompt, provider="ollama"):
    if provider == "ollama":
        return call_ollama(prompt)
    elif provider == "together":
        return call_together(prompt)
    elif provider == "groq":
        return call_groq(prompt)
    elif provider == "deepseek":
        return call_openrouter(prompt, "deepseek-chat")
    else:
        return "Unsupported provider."

def call_ollama(prompt):
    response = requests.post(OLLAMA_API_URL, json={
#response = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral",
        "prompt": prompt,
        "options": {
            "num_predict": 100
        },
        "stream": False
    })
    return response.json().get("response", "Error from Ollama")

def clean_think_tags(text: str) -> str:
    # Removes empty <think></think> blocks
    return re.sub(r"<think>\s*</think>", "", text).strip()

def call_together(prompt):
    try:
        response = together_client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.choices[0].message.content
        return clean_think_tags(content)
    except Exception as e:
        return f"Error from Together SDK: {str(e)}"


#def call_together(prompt):
#    try:
#        response = together_client.chat.completions.create(
#            model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
#            messages=[{"role": "user", "content": prompt}],
#        )
#        content = response.choices[0].message.content
#
#        # Clean out <think>...</think> tags
#        content = re.sub(r"<think>.*?</think>", "", content, flags=re.DOTALL).strip()
#        return content 
#
#
#
#        #return response.choices[0].message.content
#    except Exception as e:
#        return f"Error from Together SDK: {str(e)}"

#    headers = {
#        "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
#        "Content-Type": "application/json"
#    }
#    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json={
#        "model": "mistralai/Mistral-7B-Instruct-v0.2",
#        "messages": [{"role": "user", "content": prompt}]
#    })
#    return response.json()["choices"][0]["message"]["content"]

def call_groq(prompt):
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }
    response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json={
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    })
    return response.json()["choices"][0]["message"]["content"]

def call_openrouter(prompt, model):
    headers = {
        "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
        "Content-Type": "application/json"
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json={
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    })
    return response.json()["choices"][0]["message"]["content"]
