import streamlit as st

st.set_page_config(page_title="About | Cosmos", page_icon="ℹ️", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0d0d1a 0%, #1a0d2e 50%, #0d1a2e 100%); color: #e2e8f0; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #13132b 0%, #1e1340 100%); border-right: 1px solid rgba(139,92,246,0.3); }
    .page-header { font-size: 2.2rem; font-weight: 700;
        background: linear-gradient(90deg, #60a5fa, #34d399);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.3rem; }
    .tech-card { background: rgba(255,255,255,0.04); border: 1px solid rgba(96,165,250,0.25);
        border-radius: 14px; padding: 1.2rem 1.5rem; margin-bottom: 0.8rem; }
    .tech-name { font-weight: 600; color: #60a5fa; font-size: 1rem; }
    .tech-desc { color: #94a3b8; font-size: 0.9rem; margin-top: 0.2rem; }
    .timeline-item { border-left: 2px solid rgba(139,92,246,0.5); padding-left: 1.2rem; margin-bottom: 1.2rem; }
    .timeline-dot { width: 10px; height: 10px; background: #a78bfa; border-radius: 50%;
        margin-left: -1.6rem; float: left; margin-top: 0.4rem; margin-right: 0.8rem; }
    .timeline-title { font-weight: 600; color: #e2e8f0; }
    .timeline-desc  { color: #94a3b8; font-size: 0.9rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="page-header">ℹ️ About Cosmos Dashboard</div>', unsafe_allow_html=True)
st.markdown("Everything you need to know about this project.")
st.markdown("---")

col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown("### 🗺️ How Streamlit Multipage Apps Work")
    st.markdown(
        """
        Streamlit's multipage feature works by placing a **main entrypoint file** (e.g. `Home.py`) at
        the project root and creating a **`pages/`** folder alongside it.

        ```
        Streamlit2/
        ├── Home.py            ← entrypoint (shown first)
        └── pages/
            ├── 1_📊_Analytics.py
            ├── 2_🌍_World_Map.py
            ├── 3_🤖_AI_Studio.py
            └── 4_ℹ️_About.py
        ```

        Streamlit **automatically** discovers files in `pages/` and builds a sidebar navigation menu:

        - **File naming**: `<order>_<emoji>_<Title>.py` — the number controls sort order,
          the emoji becomes the page icon, and underscores become spaces.
        - **Each page** is a standard Python script that calls `st.set_page_config()` first.
        - **Shared state** between pages is handled via `st.session_state`.
        """
    )

    st.markdown("### 📅 Project Timeline")
    timeline = [
        ("v1.0", "Initial project scaffold with Home page."),
        ("v1.1", "Added Analytics page with Altair charts & KPI cards."),
        ("v1.2", "Introduced World Map page powered by PyDeck."),
        ("v1.3", "Built AI Studio with streaming simulation."),
        ("v1.4", "Polished CSS theming across all pages."),
    ]
    for version, desc in timeline:
        st.markdown(
            f'<div class="timeline-item">'
            f'<span class="timeline-dot"></span>'
            f'<span class="timeline-title">{version}</span><br>'
            f'<span class="timeline-desc">{desc}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )

with col_right:
    st.markdown("### 🛠️ Tech Stack")
    stack = [
        ("🐍 Python 3.11", "Core language for all app logic."),
        ("🎈 Streamlit", "Web framework & multipage routing."),
        ("🐼 Pandas", "Data manipulation & tabular display."),
        ("🔢 NumPy", "Numerical computing & synthetic data."),
        ("📈 Altair", "Declarative statistical visualisation."),
        ("🗺️ PyDeck", "WebGL-powered geospatial mapping."),
    ]
    for name, desc in stack:
        st.markdown(
            f'<div class="tech-card">'
            f'<div class="tech-name">{name}</div>'
            f'<div class="tech-desc">{desc}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown("### 🚀 Run Locally")
    st.code("streamlit run Home.py", language="bash")

    st.success("✅ All pages share the same CSS design system and color palette.")
