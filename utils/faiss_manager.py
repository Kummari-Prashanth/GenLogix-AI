import faiss
import numpy as np

index = faiss.IndexFlatL2(384)
documents = []

def add_document(text, embedding):
    index.add(np.array([embedding]).astype("float32"))
    documents.append(text)

def search(query_embedding, k=3):

    if len(documents) == 0:
        return ["No documents uploaded yet. Please upload a PDF first."]

    _, ids = index.search(
        np.array([query_embedding]).astype("float32"),
        k
    )

    results = []

    for i in ids[0]:
        if 0 <= i < len(documents):
            results.append(documents[i])

    return results