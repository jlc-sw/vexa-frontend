import requests
import os

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
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "mistral",
        "prompt": prompt,
        "options": {
            "num_predict": 100
        },
        "stream": False
    })
    return response.json().get("response", "Error from Ollama")

def call_together(prompt):
    headers = {
        "Authorization": f"Bearer {os.getenv('TOGETHER_API_KEY')}",
        "Content-Type": "application/json"
    }
    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json={
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [{"role": "user", "content": prompt}]
    })
    return response.json()["choices"][0]["message"]["content"]

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
