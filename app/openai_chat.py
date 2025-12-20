import os
import requests
import urllib3

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("OPENROUTER_MODEL", "openai/gpt-3.5-turbo")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def perguntar_openai(pergunta: str) -> str:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY não configurada")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # opcional mas recomendado pelo OpenRouter
        "HTTP-Referer": "http://localhost",
        "X-Title": "Chatbot MVP"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Você é um assistente educado e prestativo."},
            {"role": "user", "content": pergunta}
        ]
    }

    response = requests.post(
        OPENROUTER_URL,
        json=payload,
        headers=headers,
        timeout=30,
        verify=False  # ⚠️ DESATIVA verificação SSL (apenas para teste)
    )


    if response.status_code != 200:
        raise RuntimeError(f"Erro OpenRouter: {response.text}")

    data = response.json()
    return data["choices"][0]["message"]["content"]
