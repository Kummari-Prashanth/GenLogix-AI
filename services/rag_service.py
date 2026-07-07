from utils.pdf_loader import load_pdf
from utils.embeddings import create_embedding
from utils.faiss_manager import add_document, search

def upload_pdf(file):
    text = load_pdf(file)

    chunks = [text[i:i+500] for i in range(0, len(text), 500)]

    for chunk in chunks:
        embedding = create_embedding(chunk)
        add_document(chunk, embedding)

def retrieve(query):
    embedding = create_embedding(query)
    results = search(embedding)
    return "\n".join(results)