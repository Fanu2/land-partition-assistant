import streamlit as st
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from build_index import build_faiss_index
from utils import highlight_text, format_response

# --- App Config ---
st.set_page_config(page_title="Land Partition Assistant", layout="wide")
st.title("🏞️ Land Partition Assistant (Powered by Mistral via Ollama)")

# --- Load FAISS Index ---
@st.cache_resource
def load_index():
    return build_faiss_index("haryana_land_revenue_act.pdf")

index = load_index()
retriever = index.as_retriever(search_kwargs={"k": 5})

# --- Local LLM via Ollama ---
llm = Ollama(model="mistral")
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# --- UI ---
query = st.text_input("🔍 Ask a legal question", placeholder="e.g., What is the procedure for land mutation?")
if query:
    with st.spinner("Generating answer..."):
        response = qa_chain.run(query)
        st.markdown("### 📘 Answer")
        st.write(format_response(response))
        st.markdown("### 🔍 Source Highlights")
        st.write(highlight_text(response, query))
