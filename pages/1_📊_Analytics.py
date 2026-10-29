import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Analytics | Cosmos", page_icon="📊", layout="wide")

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0d0d1a 0%, #1a0d2e 50%, #0d1a2e 100%); color: #e2e8f0; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #13132b 0%, #1e1340 100%); border-right: 1px solid rgba(139,92,246,0.3); }
    .page-header { font-size: 2.2rem; font-weight: 700;
        background: linear-gradient(90deg, #a78bfa, #60a5fa);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.3rem; }
    .kpi-card { background: rgba(139,92,246,0.12); border: 1px solid rgba(139,92,246,0.3);
        border-radius: 14px; padding: 1.3rem; text-align: center; }
    .kpi-value { font-size: 2rem; font-weight: 700; color: #a78bfa; }
    .kpi-label { font-size: 0.85rem; color: #64748b; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="page-header">📊 Analytics</div>', unsafe_allow_html=True)
st.markdown("Real-time style charts generated from synthetic data.")
st.markdown("---")

# ── Sidebar controls ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚙️ Controls")
    days   = st.slider("Days of data", 30, 365, 90)
    metric = st.selectbox("Primary metric", ["Revenue", "Users", "Sessions", "Conversions"])
    noise  = st.slider("Noise level", 0.0, 1.0, 0.3)

# ── Generate synthetic data ───────────────────────────────────────────────────
np.random.seed(42)
dates  = pd.date_range(end=pd.Timestamp.today(), periods=days)
trend  = np.linspace(1000, 5000, days)
series = trend + trend * noise * np.random.randn(days)
df     = pd.DataFrame({"date": dates, metric: np.abs(series)})

# ── KPI Strip ─────────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
kpis = [
    (f"{df[metric].iloc[-1]:,.0f}", f"Latest {metric}"),
    (f"{df[metric].mean():,.0f}",   f"Avg {metric}"),
    (f"{df[metric].max():,.0f}",    f"Peak {metric}"),
    (f"{((df[metric].iloc[-1]-df[metric].iloc[0])/df[metric].iloc[0]*100):+.1f}%", "Growth"),
]
for col, (val, label) in zip([k1, k2, k3, k4], kpis):
    col.markdown(
        f'<div class="kpi-card"><div class="kpi-value">{val}</div>'
        f'<div class="kpi-label">{label}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# ── Area chart ────────────────────────────────────────────────────────────────
area = (
    alt.Chart(df)
    .mark_area(
        line={"color": "#a78bfa"},
        color=alt.Gradient(
            gradient="linear",
            stops=[
                alt.GradientStop(color="rgba(167,139,250,0.6)", offset=0),
                alt.GradientStop(color="rgba(167,139,250,0.0)", offset=1),
            ],
            x1=1, x2=1, y1=1, y2=0,
        ),
    )
    .encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y(f"{metric}:Q", title=metric),
        tooltip=["date:T", f"{metric}:Q"],
    )
    .properties(height=320, title=f"{metric} Over Time")
    .configure_axis(labelColor="#94a3b8", titleColor="#94a3b8", gridColor="rgba(255,255,255,0.05)")
    .configure_title(color="#e2e8f0")
    .configure_view(strokeOpacity=0)
)
st.altair_chart(area, use_container_width=True)

# ── Histogram ─────────────────────────────────────────────────────────────────
st.markdown("#### Distribution")
hist = (
    alt.Chart(df)
    .mark_bar(color="#60a5fa", opacity=0.8)
    .encode(
        x=alt.X(f"{metric}:Q", bin=alt.Bin(maxbins=30), title=metric),
        y=alt.Y("count()", title="Frequency"),
    )
    .properties(height=220)
    .configure_axis(labelColor="#94a3b8", titleColor="#94a3b8", gridColor="rgba(255,255,255,0.05)")
    .configure_view(strokeOpacity=0)
)
st.altair_chart(hist, use_container_width=True)

# ── Raw data toggle ───────────────────────────────────────────────────────────
with st.expander("🔍 View Raw Data"):
    st.dataframe(df.set_index("date").style.highlight_max(color="#3b1f6b"), use_container_width=True)
