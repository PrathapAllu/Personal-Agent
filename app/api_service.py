import ollama

EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen3.5:4b"

def embed(text: str) -> list[float]:
    res = ollama.embed(model=EMBED_MODEL, input=text)
    return res["embeddings"][0]

def chat(prompt: str) -> str:
    res = ollama.chat(
        model=CHAT_MODEL,
        messages=[{"role": "user", "content": prompt}],
    )
    return res["message"]["content"]