import streamlit as st
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from build_index import build_faiss_index
from utils import highlight_text, format_response

# --- App Config ---
st.set_page_config(page_title="Land Partition Assistant", layout="wide")
st.title("🏞️ Land Partition Assistant")
st.markdown("Ask questions about the Haryana Land Revenue Act or mutation records.")

# --- Load Data ---
@st.cache_resource
def load_index():
    return build_faiss_index("haryana_land_revenue_act.pdf")

@st.cache_data
def load_mutation_data():
    return pd.read_csv("sample_mutation_records.csv")

# --- Initialize Models ---
index = load_index()
retriever = index.as_retriever(search_kwargs={"k": 5})
llm = ChatOpenAI(temperature=0.2)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# --- Sidebar ---
st.sidebar.header("Mutation Record Viewer")
mutation_df = load_mutation_data()
selected_record = st.sidebar.selectbox("Choose a record", mutation_df["Record ID"].astype(str))

if selected_record:
    record_data = mutation_df[mutation_df["Record ID"].astype(str) == selected_record].to_dict(orient="records")[0]
    st.sidebar.write("### Record Details")
    for key, value in record_data.items():
        st.sidebar.write(f"**{key}**: {value}")

# --- Main QA Section ---
query = st.text_input("🔍 Ask a legal question", placeholder="e.g., What is the procedure for land mutation?")
if query:
    with st.spinner("Thinking..."):
        response = qa_chain.run(query)
        st.markdown("### 📘 Answer")
        st.write(format_response(response))
        st.markdown("### 🔍 Source Highlights")
        st.write(highlight_text(response, query))
