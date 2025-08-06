import streamlit as st
import pandas as pd
from utils import filter_records, generate_notice

st.set_page_config(page_title="Land Partition Assistant", layout="wide")

st.title("📜 Haryana Land Partition Assistant – Section 111A")

with st.expander("🔍 What is Section 111A?"):
    st.markdown("""
    Section 111A empowers Revenue Officers to initiate partition of jointly held land by mutual consent...
    - Applies to all co-sharers except husband-wife
    - 6-month timeline + 6-month extension
    - Mutation updates under Section 123
    """)

st.subheader("📋 Generate Suo Motu Notice")
name = st.text_input("Enter Co-sharer Name")
relation = st.selectbox("Relation to Other Co-sharers", ["Sibling", "Parent", "Spouse", "Other"])
if st.button("Generate Notice"):
    if relation == "Spouse":
        st.warning("Partition not applicable for husband-wife under Section 111A.")
    else:
        st.success(generate_notice(name, relation))

st.subheader("📊 View Mutation Records")
uploaded_file = st.file_uploader("Upload mutation CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    filtered_df = filter_records(df)
    st.dataframe(filtered_df)
