# Coffee Roasting Companion

A RAG-powered (Retrieval-Augmented Generation) coffee roasting assistant for home roasters and coffee enthusiasts. Ask anything about bean origins, roasting science, troubleshooting, equipment, and brewing, and get grounded, knowledgeable answers pulled from a curated knowledge base.

**[Live Demo](https://richmarra-coffee-roasting-companion.streamlit.app)** | **Portfolio Project 4 of 5** | [Full Portfolio](https://github.com/richmarra1)

---

## What This Does

You ask a coffee roasting question. The app retrieves the most relevant documents from a 25-document knowledge base using BM25 ranking, injects that context into a Claude API prompt, and generates a response that is grounded in real coffee roasting knowledge rather than relying solely on the LLM's training data. Every response shows which source documents were retrieved, making the RAG pipeline transparent and auditable.

The knowledge base covers eight domains: bean origins and flavor profiles (Ethiopia, Colombia, Brazil, Sumatra, Guatemala, Kenya, Costa Rica), roasting science (Maillard reaction, caramelization, bean density, first and second crack), roast levels (light through dark with specific temperatures and flavor characteristics), home roasting methods and equipment (popcorn poppers through the Aillio Bullet), troubleshooting (underdeveloped, baked, scorched, uneven, smoky), brewing fundamentals (rest periods, grind size, water quality), coffee culture and fun facts, and a structured beginner roadmap.

---

## Architecture: Why RAG?

This project introduces a fundamentally different AI architecture from the other projects in this portfolio.

| Dimension | Project 1: SaaS Agent | Project 2: Telerad Ops | Project 3: GPT | Project 4: Coffee Companion |
|---|---|---|---|---|
| **Architecture** | Probabilistic pipeline | Deterministic tree | Prompt engineering | RAG (retrieval + generation) |
| **Knowledge** | LLM training data | Hardcoded knowledge base | LLM + instructions | Retrieved from curated docs |
| **Grounding** | None (pure generation) | Complete (deterministic) | Instruction-based | Document-grounded |
| **Transparency** | Low | High | Low | High (sources shown) |

RAG solves a specific problem: LLMs can hallucinate. When you ask a general LLM about coffee roasting, it might generate plausible-sounding advice that is technically wrong. RAG grounds the response in vetted, curated content. The user can see exactly which documents informed the answer. This is the same pattern used in enterprise knowledge management, customer support, and healthcare information systems where accuracy matters more than creativity.

---

## How the Retrieval Works

The retriever uses BM25 (Best Matching 25), a proven information retrieval algorithm that ranks documents by term frequency, inverse document frequency, and document length normalization. For each user query:

1. The query is tokenized and stopwords are removed
2. Each document in the knowledge base is scored using BM25 with title boosting (title matches weighted 2x)
3. The top 3 documents are retrieved and injected into the Claude API prompt as grounding context
4. Claude generates a response constrained to the retrieved information
5. Source documents are displayed to the user with relevance scores

This lightweight approach was chosen over vector embeddings because the knowledge base is small enough (25 documents) that BM25 performs well without the infrastructure overhead of a vector database. For a larger knowledge base (hundreds or thousands of documents), you would upgrade to dense retrieval with embeddings.

---

## Tech Stack

- **Python 3.11+**
- **Streamlit** - Application framework
- **Anthropic Claude API** - Response generation (claude-sonnet-4-20250514)
- **BM25 Retrieval** - Custom implementation, no external dependencies
- **25-document knowledge base** across 8 domains
- **DM Serif Display / Inter / JetBrains Mono** - Typography

---

## Project Structure

```
coffee-roasting-llm/
├── app.py                           # Streamlit app with RAG pipeline
├── knowledge/
│   ├── __init__.py
│   └── coffee_knowledge.py          # 25-document curated knowledge base
├── requirements.txt
├── .streamlit/
│   └── config.toml                  # Warm coffee theme
├── .devcontainer/
│   └── devcontainer.json
├── .gitignore
└── README.md
```

---

## Run Locally

```bash
git clone https://github.com/richmarra1/coffee-roasting-companion.git
cd coffee-roasting-companion
pip install -r requirements.txt
export ANTHROPIC_API_KEY=your_key_here
streamlit run app.py
```

---

## About

Built by [Rich Marra](https://www.linkedin.com/in/richmarra/) as part of an applied AI portfolio demonstrating range across architectures: probabilistic pipelines, deterministic logic, prompt engineering, and retrieval-augmented generation. Each project solves a different problem with the architecture that fits, not the architecture that is trending.
