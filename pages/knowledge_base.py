import streamlit as st
from services.rag_service import upload_pdf

def show_knowledge_base():

    st.title("Knowledge Base")

    pdf = st.file_uploader(
        "Upload Logistics PDF",
        type=["pdf"]
    )

    if pdf:
        upload_pdf(pdf)
        st.success("PDF uploaded successfully!")