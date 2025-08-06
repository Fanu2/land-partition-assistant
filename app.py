import streamlit as st
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from build_index import build_faiss_index
from utils import highlight_text, format_response
from sentence_transformers import SentenceTransformer
from langchain.embeddings import HuggingFaceEmbeddings

# --- App Config ---
st.set_page_config(page_title="Land Partition Assistant", layout="wide")
st.title("🏞️ Land Partition Assistant (No API Key Required)")

# --- Load FAISS Index ---
@st.cache_resource
def load_index():
    return build_faiss_index("haryana_land_revenue_act.pdf")

index = load_index()
retriever = index.as_retriever(search_kwargs={"k": 5})

# --- Simple Retrieval-Based QA ---
def basic_qa(query):
    docs = retriever.get_relevant_documents(query)
    return "\n\n".join([doc.page_content for doc in docs[:3]])

# --- UI ---
query = st.text_input("🔍 Ask a legal question", placeholder="e.g., What is the procedure for land mutation?")
if query:
    with st.spinner("Searching..."):
        response = basic_qa(query)
        st.markdown("### 📘 Answer")
        st.write(format_response(response))
        st.markdown("### 🔍 Source Highlights")
        st.write(highlight_text(response, query))
