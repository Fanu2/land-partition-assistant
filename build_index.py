from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from sentence_transformers import SentenceTransformer
from langchain_community.embeddings import HuggingFaceEmbeddings

def build_faiss_index(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(pages)

    # Use free Hugging Face embeddings
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model_name)

    return FAISS.from_documents(docs, embeddings)
