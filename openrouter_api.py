# openrouter_api.py

import requests
from config import HEADERS, MODEL_NAME

def call_openrouter(prompt: str) -> str:
    body = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}]
    }
    res = requests.post("https://openrouter.ai/api/v1/chat/completions",
                        headers=HEADERS, json=body)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]
