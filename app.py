"""
Coffee Roasting Companion
===========================
RAG-powered coffee roasting assistant for home roasters.
Retrieves relevant knowledge from a curated coffee roasting
knowledge base and generates grounded responses via Claude API.
"""

import streamlit as st
import os
import re
import math
from collections import Counter
from anthropic import Anthropic

# Import knowledge base
from knowledge.coffee_knowledge import KNOWLEDGE_BASE

# ---------------------------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Coffee Roasting Companion",
    page_icon="☕",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Custom CSS - Warm light coffee theme
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    .stApp {
        background: #faf6f1 !important;
    }
    .block-container { padding-top: 1rem; max-width: 860px; }
    h1, h2, h3, h4, h5, h6, p, li, span, div { font-family: 'Inter', sans-serif !important; }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}

    /* Header */
    .app-header {
        display: flex; align-items: center; gap: 16px;
        padding: 24px 0 8px;
    }
    .app-logo {
        width: 48px; height: 48px; border-radius: 12px;
        background: linear-gradient(135deg, #8b6f47 0%, #6b5234 100%);
        display: flex; align-items: center; justify-content: center;
        font-size: 24px; flex-shrink: 0;
        box-shadow: 0 4px 16px rgba(107,82,52,0.2);
    }
    .app-title {
        font-family: 'DM Serif Display', serif !important;
        font-size: 24px; font-weight: 400; color: #3d2e1f;
        letter-spacing: -0.02em;
    }
    .app-subtitle { font-size: 12px; color: #8b7355; margin-top: 2px; }

    /* Chat bubbles */
    .assistant-bubble {
        background: #ffffff; border: 1px solid #e8dfd4;
        border-radius: 2px 18px 18px 18px; padding: 18px 22px;
        font-size: 14px; line-height: 1.75; color: #3d2e1f;
        max-width: 90%; margin-bottom: 14px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.04);
    }
    .assistant-label {
        font-size: 9px; font-weight: 700; text-transform: uppercase;
        letter-spacing: 0.12em; color: #8b6f47; margin-bottom: 8px;
        display: flex; align-items: center; gap: 6px;
    }
    .user-bubble {
        background: linear-gradient(135deg, #8b6f47 0%, #6b5234 100%);
        border-radius: 18px 2px 18px 18px; padding: 12px 20px;
        font-size: 14px; line-height: 1.5; color: #ffffff;
        max-width: 75%; margin-left: auto; margin-bottom: 14px;
        text-align: right;
    }

    /* Source cards */
    .source-card {
        background: #f5efe8; border: 1px solid #e8dfd4;
        border-radius: 8px; padding: 10px 14px; margin-top: 4px; margin-bottom: 4px;
        font-size: 11px; color: #6b5540;
    }
    .source-title { font-weight: 600; color: #5c3d2e; font-size: 12px; }
    .source-domain {
        display: inline-block; padding: 2px 8px; border-radius: 4px;
        background: #ebe3d7; font-size: 9px;
        font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em;
        color: #8b6f47;
    }

    /* Topic cards */
    .topic-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin: 14px 0; }
    .topic-card {
        background: #ffffff; border: 1px solid #e8dfd4;
        border-radius: 12px; padding: 16px; cursor: pointer; transition: all 0.2s;
    }
    .topic-card:hover { background: #f5efe8; border-color: #c8a27a; }
    .topic-icon { font-size: 22px; margin-bottom: 6px; }
    .topic-label { font-size: 13px; font-weight: 600; color: #3d2e1f; margin-bottom: 4px; }
    .topic-desc { font-size: 11px; color: #8b7355; line-height: 1.4; }

    /* Input styling */
    .stChatInput > div { background: #ffffff !important; border-color: #e8dfd4 !important; }
    .stChatInput textarea { color: #3d2e1f !important; font-family: 'Inter', sans-serif !important; }

    /* Button overrides */
    .stButton > button {
        background: #ffffff !important; border: 1px solid #e8dfd4 !important;
        border-radius: 10px !important; padding: 10px 16px !important;
        font-size: 13px !important; color: #5c3d2e !important;
        font-family: 'Inter', sans-serif !important; width: 100% !important;
        text-align: left !important;
    }
    .stButton > button:hover {
        background: #f5efe8 !important;
        border-color: #c8a27a !important;
        color: #3d2e1f !important;
    }

    /* Sidebar */
    .css-1d391kg, [data-testid="stSidebar"] { background: #faf6f1 !important; }

    /* Footer */
    .app-footer {
        text-align: center; padding: 40px 0 20px;
        font-size: 11px; color: #c8b89e;
    }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Lightweight BM25-style Retriever
# ---------------------------------------------------------------------------
def tokenize(text):
    """Simple tokenizer: lowercase, split on non-alphanumeric, remove stopwords."""
    stopwords = {
        'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
        'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
        'should', 'may', 'might', 'shall', 'can', 'need', 'dare', 'ought',
        'used', 'to', 'of', 'in', 'for', 'on', 'with', 'at', 'by', 'from',
        'as', 'into', 'through', 'during', 'before', 'after', 'above', 'below',
        'between', 'out', 'off', 'over', 'under', 'again', 'further', 'then',
        'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'both',
        'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
        'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'just',
        'and', 'but', 'or', 'if', 'while', 'that', 'this', 'these', 'those',
        'it', 'its', 'they', 'them', 'their', 'what', 'which', 'who', 'whom',
        'i', 'me', 'my', 'we', 'our', 'you', 'your', 'he', 'him', 'his',
        'she', 'her', 'about',
    }
    tokens = re.findall(r'[a-z0-9]+', text.lower())
    return [t for t in tokens if t not in stopwords and len(t) > 1]


def build_index(documents):
    """Build inverted index and document frequency counts for BM25."""
    doc_tokens = []
    df = Counter()
    for doc in documents:
        text = doc['title'] + ' ' + doc['content']
        tokens = tokenize(text)
        doc_tokens.append(tokens)
        unique_tokens = set(tokens)
        for t in unique_tokens:
            df[t] += 1
    return doc_tokens, df


def bm25_score(query_tokens, doc_tokens, df, n_docs, k1=1.5, b=0.75, avgdl=None):
    """Calculate BM25 score for a single document."""
    if avgdl is None:
        avgdl = 200
    dl = len(doc_tokens)
    tf_map = Counter(doc_tokens)
    score = 0.0
    for qt in query_tokens:
        if qt in tf_map:
            tf = tf_map[qt]
            doc_freq = df.get(qt, 0)
            idf = math.log((n_docs - doc_freq + 0.5) / (doc_freq + 0.5) + 1)
            tf_norm = (tf * (k1 + 1)) / (tf + k1 * (1 - b + b * dl / avgdl))
            score += idf * tf_norm
    return score


def retrieve(query, documents, doc_tokens_list, df, top_k=3):
    """Retrieve the top-k most relevant documents for a query."""
    query_tokens = tokenize(query)
    n_docs = len(documents)
    avgdl = sum(len(dt) for dt in doc_tokens_list) / max(n_docs, 1)

    scores = []
    for i, doc in enumerate(documents):
        # Boost title matches
        title_tokens = tokenize(doc['title'])
        title_score = bm25_score(query_tokens, title_tokens, df, n_docs, avgdl=10)
        content_score = bm25_score(query_tokens, doc_tokens_list[i], df, n_docs, avgdl=avgdl)
        combined = content_score + title_score * 2.0
        scores.append((combined, i))

    scores.sort(reverse=True, key=lambda x: x[0])
    results = []
    for score, idx in scores[:top_k]:
        if score > 0:
            results.append({
                "score": score,
                "document": documents[idx]
            })
    return results


# ---------------------------------------------------------------------------
# Build index at startup
# ---------------------------------------------------------------------------
@st.cache_data
def initialize_retriever():
    doc_tokens, df = build_index(KNOWLEDGE_BASE)
    return doc_tokens, df

DOC_TOKENS, DF = initialize_retriever()


# ---------------------------------------------------------------------------
# Domain labels for display
# ---------------------------------------------------------------------------
DOMAIN_LABELS = {
    "origins": "Bean Origins",
    "roasting_science": "Roasting Science",
    "roast_levels": "Roast Levels",
    "home_roasting": "Home Roasting",
    "troubleshooting": "Troubleshooting",
    "brewing": "Brewing",
    "fun_facts": "Coffee Culture",
    "beginner": "Getting Started",
}

DOMAIN_ICONS = {
    "origins": "🌍",
    "roasting_science": "🔬",
    "roast_levels": "🎨",
    "home_roasting": "🏠",
    "troubleshooting": "🔧",
    "brewing": "☕",
    "fun_facts": "✨",
    "beginner": "🚀",
}


# ---------------------------------------------------------------------------
# Generate response with Claude API + RAG context
# ---------------------------------------------------------------------------
def generate_response(user_message, retrieved_docs, chat_history):
    """Generate a response using Claude API with retrieved context."""
    api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return "Please set your ANTHROPIC_API_KEY in the app secrets to enable AI responses.", []

    client = Anthropic(api_key=api_key)

    # Build context from retrieved documents
    context_parts = []
    for r in retrieved_docs:
        doc = r["document"]
        context_parts.append(f"[{doc['title']}]\n{doc['content']}")
    context_block = "\n\n---\n\n".join(context_parts)

    system_prompt = f"""You are the Coffee Roasting Companion, a friendly, knowledgeable guide for home coffee roasters. You are like that friend at a coffee shop who genuinely geeks out about roasting and wants to help everyone discover the joy of roasting their own coffee.

YOUR PERSONALITY:
- Warm, enthusiastic, and approachable. Never condescending
- You use casual but informed language. Not academic, not dumbed-down
- You share the "why" behind things, not just the "what"
- You encourage experimentation. There is no single right way to roast
- You celebrate the journey. A beginner's first roast is worth being excited about
- You use sensory language: talk about aromas, colors, sounds, and flavors
- Sprinkle in fun facts and coffee culture when it adds to the conversation
- Keep responses focused and conversational. Not walls of text

GROUNDING RULES:
- Base your responses on the retrieved knowledge below
- If the retrieved context does not cover the question, say so honestly and share what you do know
- Do not make up specific temperatures, times, or technical claims that are not in the context
- When discussing origins, processing methods, or roasting science, stay grounded in the retrieved information

RETRIEVED KNOWLEDGE:
{context_block}

FORMATTING:
- Default to conversational prose, not bullet lists
- Keep responses to 2-4 paragraphs unless the user asks for more detail
- Use specific, concrete language over vague generalities
- If comparing things (origins, roast levels, methods), a brief structured comparison is fine"""

    # Build messages from chat history
    messages = []
    for msg in chat_history:
        messages.append({"role": msg["role"], "content": msg["content"]})
    messages.append({"role": "user", "content": user_message})

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system_prompt,
            messages=messages
        )
        return response.content[0].text, retrieved_docs
    except Exception as e:
        return f"I had trouble connecting to my brain. Error: {str(e)}", []


# ---------------------------------------------------------------------------
# Session State
# ---------------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "sources" not in st.session_state:
    st.session_state.sources = {}


# ---------------------------------------------------------------------------
# Render Functions
# ---------------------------------------------------------------------------
def render_sources(sources, msg_idx):
    """Render source cards for a response."""
    if sources:
        with st.expander(f"📚 Sources ({len(sources)} documents retrieved)", expanded=False):
            for s in sources:
                doc = s["document"]
                domain = doc.get("domain", "general")
                icon = DOMAIN_ICONS.get(domain, "📄")
                label = DOMAIN_LABELS.get(domain, domain)
                st.markdown(f"""
                <div class="source-card">
                    <span class="source-domain">{icon} {label}</span>
                    <div class="source-title" style="margin-top: 6px;">{doc['title']}</div>
                    <div style="margin-top: 4px; font-size: 11px; color: #6b5540;">
                        Relevance score: {s['score']:.1f} | ID: {doc['id']}
                    </div>
                </div>
                """, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------------------
st.markdown("""
<div class="app-header">
    <div class="app-logo">☕</div>
    <div>
        <div class="app-title">Coffee Roasting Companion</div>
        <div class="app-subtitle">RAG-powered guide for home coffee roasters | Ask anything about roasting, beans, and brewing</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Architecture badge
st.markdown("""
<div style="display: flex; gap: 8px; margin: 10px 0 20px; flex-wrap: wrap;">
    <span style="display: inline-block; padding: 3px 10px; border-radius: 4px; background: #ebe3d7; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #8b6f47;">RAG Architecture</span>
    <span style="display: inline-block; padding: 3px 10px; border-radius: 4px; background: #ebe3d7; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #8b6f47;">25 Knowledge Documents</span>
    <span style="display: inline-block; padding: 3px 10px; border-radius: 4px; background: #ebe3d7; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #8b6f47;">8 Domains</span>
    <span style="display: inline-block; padding: 3px 10px; border-radius: 4px; background: #ebe3d7; font-size: 9px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #8b6f47;">Claude API</span>
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Chat History
# ---------------------------------------------------------------------------
for i, msg in enumerate(st.session_state.messages):
    if msg["role"] == "assistant":
        st.markdown(f"""
        <div class="assistant-bubble">
            <div class="assistant-label">☕ Coffee Roasting Companion</div>
            {msg['content']}
        </div>
        """, unsafe_allow_html=True)
        # Render sources if available
        if i in st.session_state.sources:
            render_sources(st.session_state.sources[i], i)
    else:
        st.markdown(f"""
        <div class="user-bubble">{msg['content']}</div>
        """, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Welcome & Topic Suggestions (only if no messages yet)
# ---------------------------------------------------------------------------
if not st.session_state.messages:
    st.markdown("""
    <div class="assistant-bubble">
        <div class="assistant-label">☕ Coffee Roasting Companion</div>
        Hey! I am your Coffee Roasting Companion, here to help you learn everything about roasting coffee at home. Whether you are thinking about your first roast or trying to troubleshoot that batch that came out tasting like cardboard, I have got you covered. I pull from a curated knowledge base of roasting science, bean origins, brewing tips, and beginner guides to give you grounded, useful answers. What do you want to explore?
    </div>
    """, unsafe_allow_html=True)

    topics = [
        {"icon": "🚀", "label": "My First Roast", "desc": "Step-by-step guide to roasting your first batch", "query": "How do I roast coffee at home for the first time?"},
        {"icon": "🌍", "label": "Bean Origins", "desc": "How growing region shapes what is in your cup", "query": "What are the major coffee growing regions and how do they taste different?"},
        {"icon": "🔬", "label": "Roasting Science", "desc": "What is actually happening inside the bean?", "query": "What happens during the coffee roasting process? Explain the stages and the chemistry."},
        {"icon": "🔧", "label": "Fix My Roast", "desc": "Troubleshoot sour, flat, or bitter coffee", "query": "My home roasted coffee tastes sour and grassy. What am I doing wrong?"},
        {"icon": "🏠", "label": "Equipment Guide", "desc": "From popcorn poppers to the Aillio Bullet", "query": "What equipment do I need to start roasting coffee at home?"},
        {"icon": "☕", "label": "Brewing Tips", "desc": "Get the most out of what you roasted", "query": "How should I brew my home roasted coffee? What grind size and rest time?"},
    ]

    cols = st.columns(2)
    for i, topic in enumerate(topics):
        with cols[i % 2]:
            if st.button(f"{topic['icon']} {topic['label']}\n{topic['desc']}", key=f"topic_{i}"):
                st.session_state.pending_query = topic["query"]
                st.rerun()


# ---------------------------------------------------------------------------
# Handle pending query from topic buttons
# ---------------------------------------------------------------------------
if "pending_query" in st.session_state:
    query = st.session_state.pending_query
    del st.session_state.pending_query

    # Add user message
    st.session_state.messages.append({"role": "user", "content": query})

    # Retrieve
    retrieved = retrieve(query, KNOWLEDGE_BASE, DOC_TOKENS, DF, top_k=3)

    # Generate
    response_text, sources = generate_response(
        query, retrieved,
        [m for m in st.session_state.messages[:-1] if m["role"] in ("user", "assistant")]
    )

    # Store
    msg_idx = len(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    if sources:
        st.session_state.sources[msg_idx] = sources

    st.rerun()


# ---------------------------------------------------------------------------
# Chat Input
# ---------------------------------------------------------------------------
if prompt := st.chat_input("Ask me anything about coffee roasting..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Retrieve relevant documents
    retrieved = retrieve(prompt, KNOWLEDGE_BASE, DOC_TOKENS, DF, top_k=3)

    # Generate response
    with st.spinner("Pulling from the knowledge base..."):
        response_text, sources = generate_response(
            prompt, retrieved,
            [m for m in st.session_state.messages[:-1] if m["role"] in ("user", "assistant")]
        )

    # Store response and sources
    msg_idx = len(st.session_state.messages)
    st.session_state.messages.append({"role": "assistant", "content": response_text})
    if sources:
        st.session_state.sources[msg_idx] = sources

    st.rerun()


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown("""
<div class="app-footer">
    Built by Rich Marra | RAG Architecture with BM25 Retrieval + Claude API | Portfolio Project 4 of 5
</div>
""", unsafe_allow_html=True)
