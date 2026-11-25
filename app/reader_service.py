from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"  # change if yours is elsewhere

def load_chunks(size=500, overlap=50):
    chunks = []
    for f in DOCS_DIR.glob("*"):
        if f.suffix.lower() not in (".txt", ".md"):
            continue
        text = f.read_text(encoding="utf-8", errors="ignore")
        step = size - overlap
        for i in range(0, len(text), step):
            piece = text[i:i + size].strip()
            if piece:
                chunks.append({"source": f.name, "text": piece})
    return chunks