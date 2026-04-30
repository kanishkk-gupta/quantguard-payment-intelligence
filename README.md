# QuantGuard — Real-time Payment Intelligence System

> Multimodal Fraud Detection + Regulatory RAG + HFT-inspired Smart Routing

## Architecture
Transaction Stream
        │
        ├──→ Heatmap → CNN Encoder ──┐
        │                            ├→ Fusion → Fraud Score
        └──→ Sequence → LSTM Encoder─┘
                    │
          ┌─────────┴──────────┐
          │                    │
    FRAUD FLAGGED          CLEAN TXN
          │                    │
          ▼                    ▼
   Regulatory RAG       Thompson Sampling
   (RBI/NPCI/PCI-DSS)   Smart Gateway Router

## Stack
- PyTorch — CNN + LSTM dual encoder (from scratch)
- NumPy — Thompson Sampling bandit (from scratch)
- Sentence-Transformers — local embeddings (no API)
- FAISS + BM25 — hybrid retrieval
- Plotly Dash — live dashboard

## References
- Russo et al. (2018) — A Tutorial on Thompson Sampling
- Two Sigma Order Book Imaging Research
- RBI Master Circular on Cyber Security Framework
- Easley, López de Prado & O'Hara (2012) — VPIN

## Live Demo
https://quantguard.streamlit.app ← updating shortly

## Status
🚧 Active development
