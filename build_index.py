from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def build_faiss_index(pdf_path_or_folder):
    documents = []

    # Load single PDF or all PDFs in a folder
    if os.path.isdir(pdf_path_or_folder):
        for filename in os.listdir(pdf_path_or_folder):
            if filename.endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(pdf_path_or_folder, filename))
                documents.extend(loader.load())
    else:
        loader = PyPDFLoader(pdf_path_or_folder)
        documents = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)

    # Embed and index
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return vectorstore
