import streamlit as st
from utils.load_sample_data import load_sample_resolution

st.set_page_config(page_title="UNSC LLM Assistant", layout="wide")

st.title("🔎 UNSC Resolutions Reference LLM")
st.markdown("Ask a question or view a sample resolution.")

sample = load_sample_resolution()

tab1, tab2 = st.tabs(["Ask a Question", "View Resolution"])

with tab1:
    st.info("This is a placeholder for your Retrieval QA interface using LangChain and OpenAI.")
    st.markdown("In the full version, you'll enter a question and get an answer from UNSC documents.")

with tab2:
    st.subheader(sample["title"])
    st.markdown(f"**Symbol:** {sample['symbol']}")
    st.text_area("Resolution Text", sample["text"], height=300)
