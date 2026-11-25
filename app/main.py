import math
import ollama
from app.api_service import embed, CHAT_MODEL
from app.reader_service import load_chunks

chunks = load_chunks(size=800, overlap=150)
for c in chunks:
    c["vec"] = embed("search_document: " + c["text"])
print(f"Embedded {len(chunks)} chunks")

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b)))

def search_docs(query: str) -> str:
    """Search the user's documents and return the most relevant passages.

    Args:
        query: Keywords or a short question describing what to find.
    """
    qv = embed("search_query: " + query)
    top = sorted(chunks, key=lambda c: cosine(qv, c["vec"]), reverse=True)[:4]
    return "\n---\n".join(f"[{c['source']}] {c['text']}" for c in top)

SYSTEM = ("You answer questions about the user's documents. Use search_docs to find "
          "facts. Search again with different keywords if the first result lacks "
          "the answer. If you still can't find it, say so.")

def run_agent(question, max_steps=5):
    messages = [{"role": "system", "content": SYSTEM},
                {"role": "user", "content": question}]
    for _ in range(max_steps):
        res = ollama.chat(model=CHAT_MODEL, messages=messages,
                          tools=[search_docs], think=False)
        msg = res.message
        messages.append(msg)
        if not msg.tool_calls:
            return msg.content
        for call in msg.tool_calls:
            print("  [tool call]", call.function.name, dict(call.function.arguments))
            result = search_docs(**call.function.arguments)
            messages.append({"role": "tool", "tool_name": call.function.name,
                             "content": result})
    return "Stopped: too many steps."

while True:
    q = input("\nAsk (or 'exit'): ")
    if q == "exit":
        break
    print(run_agent(q))