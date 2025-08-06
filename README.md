# 🏛️ Land Partition Assistant – Haryana Section 111A

A civic-tech Streamlit app that simplifies land partition workflows under Section 111A of the Haryana Land Revenue Act (2025 Amendment).

## 🚀 Features

- 📖 Section 111A explainer with legal highlights
- 📋 Suo motu notice generator for Revenue Officers
- 📊 Mutation register viewer with spouse filter
- 💬 Legal Q&A chatbot using LangChain + FAISS
- 📈 Partition status dashboard with timeline tracker

## 🧠 Tech Stack

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Streamlit   | UI and dashboard                 |
| LangChain   | Legal Q&A chatbot                |
| FAISS       | Vector search for legal text     |
| OpenAI      | Embeddings + LLM                 |
| Pandas      | Data handling                    |

## 📦 Setup

```bash
git clone https://github.com/yourusername/land-partition-assistant
cd land-partition-assistant
pip install -r requirements.txt
python build_index.py  # Build FAISS index from PDF
streamlit run app.py
