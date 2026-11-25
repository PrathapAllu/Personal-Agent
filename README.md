# Personal-Agent

Personal-Agent is a personal knowledge agent for quickly asking questions about your own information. Each user can provide their documents and data, then ask questions in natural language to find relevant details and get answers grounded in that information. The goal is to make personal knowledge easy to search and useful through conversation.

## Technology

- **Python** for document processing and backend logic
- **OpenAI** for embeddings and answer generation
- **ChromaDB** for storing and searching document embeddings
- **Streamlit** for the document-upload and chat interface

## How it works

Add PDF or TXT files to build a searchable personal knowledge base. The app processes the documents, stores searchable embeddings in ChromaDB, and retrieves relevant context when you ask a question. OpenAI is planned for embeddings and answer generation; this requires an API connection and may send document content to OpenAI. A Streamlit chat interface will let users add documents and ask questions. The project is under development; setup instructions will follow once implemented.
