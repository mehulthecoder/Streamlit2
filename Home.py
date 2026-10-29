import streamlit as st

st.set_page_config(
    page_title="🌌 Cosmos Dashboard",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    /* Dark gradient background */
    .stApp {
        background: linear-gradient(135deg, #0d0d1a 0%, #1a0d2e 50%, #0d1a2e 100%);
        color: #e2e8f0;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #13132b 0%, #1e1340 100%);
        border-right: 1px solid rgba(139,92,246,0.3);
    }
    [data-testid="stSidebar"] .stMarkdown p { color: #a78bfa; }

    /* Hero card */
    .hero-card {
        background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(59,130,246,0.15));
        border: 1px solid rgba(139,92,246,0.4);
        border-radius: 20px;
        padding: 3rem 2.5rem;
        text-align: center;
        backdrop-filter: blur(10px);
        margin-bottom: 2rem;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .hero-sub {
        font-size: 1.15rem;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }

    /* Feature cards */
    .feature-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(139,92,246,0.25);
        border-radius: 16px;
        padding: 1.6rem;
        transition: transform 0.2s, border-color 0.2s;
        height: 100%;
    }
    .feature-card:hover {
        transform: translateY(-4px);
        border-color: rgba(139,92,246,0.6);
    }
    .feature-icon { font-size: 2.4rem; margin-bottom: 0.6rem; }
    .feature-title { font-size: 1.1rem; font-weight: 600; color: #e2e8f0; margin-bottom: 0.4rem; }
    .feature-desc  { font-size: 0.9rem; color: #94a3b8; line-height: 1.5; }

    /* Stats strip */
    .stat-box {
        background: rgba(139,92,246,0.12);
        border: 1px solid rgba(139,92,246,0.3);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
    }
    .stat-value { font-size: 2rem; font-weight: 700; color: #a78bfa; }
    .stat-label { font-size: 0.85rem; color: #64748b; margin-top: 0.2rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌌 Cosmos Dashboard")
    st.markdown("---")
    st.markdown("**Navigate using the pages above** ↑")
    st.markdown(
        """
        - 📊 **Analytics** — live charts & KPIs
        - 🌍 **World Map** — geospatial explorer
        - 🤖 **AI Studio** — prompt playground
        - ℹ️ **About** — project info
        """
    )
    st.markdown("---")
    st.caption("Built with ❤️ using Streamlit")

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">🌌 Cosmos Dashboard</div>
        <div class="hero-sub">A stunning multipage Streamlit app — explore data, maps & AI in one place.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Stats Strip ───────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
stats = [
    ("4", "App Pages"),
    ("∞", "Data Points"),
    ("100 ms", "Avg Load Time"),
    ("⭐ 5.0", "User Rating"),
]
for col, (val, label) in zip([c1, c2, c3, c4], stats):
    col.markdown(
        f'<div class="stat-box"><div class="stat-value">{val}</div>'
        f'<div class="stat-label">{label}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ── Feature Cards ─────────────────────────────────────────────────────────────
st.markdown("### 🚀 What's Inside")
f1, f2, f3, f4 = st.columns(4)
features = [
    ("📊", "Analytics", "Interactive time-series charts, histograms, and key performance indicators powered by Altair & Pandas."),
    ("🌍", "World Map", "Geospatial visualisation with Pydeck — explore population & country data on a 3-D globe."),
    ("🤖", "AI Studio", "A prompt playground that lets you experiment with text generation and model parameters."),
    ("ℹ️", "About", "Learn about the project architecture, tech stack, and how Streamlit multipage apps work."),
]
for col, (icon, title, desc) in zip([f1, f2, f3, f4], features):
    col.markdown(
        f'<div class="feature-card">'
        f'<div class="feature-icon">{icon}</div>'
        f'<div class="feature-title">{title}</div>'
        f'<div class="feature-desc">{desc}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)
st.info("👈 Use the **sidebar** to navigate between pages.")
