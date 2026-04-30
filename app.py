import streamlit as st

st.set_page_config(page_title="QuantGuard", page_icon="🛡️", layout="wide")

st.title("🛡️ QuantGuard — Payment Intelligence System")
st.caption("Multimodal Fraud Detection + Regulatory RAG + Smart Routing")

st.info("🚧 Full demo deploying shortly — engines being integrated")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Engine 1")
    st.markdown("**Multimodal Fraud Detection**")
    st.markdown("CNN over transaction heatmaps + LSTM over sequences → fused fraud score")

with col2:
    st.markdown("### Engine 2")
    st.markdown("**Regulatory RAG**")
    st.markdown("Hybrid BM25+FAISS retrieval over RBI/NPCI/PCI-DSS docs")

with col3:
    st.markdown("### Engine 3")
    st.markdown("**Smart Gateway Router**")
    st.markdown("Thompson Sampling bandit — routes to optimal gateway in real-time")

st.divider()
st.markdown("Built from scratch · No LLM API · No LangChain")
