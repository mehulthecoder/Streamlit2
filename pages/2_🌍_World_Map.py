import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.set_page_config(page_title="World Map | Cosmos", page_icon="🌍", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0d0d1a 0%, #1a0d2e 50%, #0d1a2e 100%); color: #e2e8f0; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #13132b 0%, #1e1340 100%); border-right: 1px solid rgba(139,92,246,0.3); }
    .page-header { font-size: 2.2rem; font-weight: 700;
        background: linear-gradient(90deg, #34d399, #60a5fa);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.3rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="page-header">🌍 World Map Explorer</div>', unsafe_allow_html=True)
st.markdown("Explore synthetic population data across major world cities on an interactive 3-D map.")
st.markdown("---")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🗺️ Map Settings")
    map_style   = st.selectbox("Style", ["dark", "satellite", "light"], index=0)
    radius      = st.slider("Bubble radius (m)", 50_000, 500_000, 150_000, 10_000)
    opacity_val = st.slider("Opacity", 0.1, 1.0, 0.6)
    show_hex    = st.checkbox("Show hexagon layer", value=False)

# ── Synthetic city data ───────────────────────────────────────────────────────
cities = pd.DataFrame({
    "city":       ["New York", "London", "Tokyo", "Sydney", "Mumbai", "São Paulo",
                   "Cairo", "Lagos", "Moscow", "Beijing", "Los Angeles", "Paris"],
    "lat":        [40.71, 51.51, 35.68, -33.87, 19.08, -23.55,
                   30.05, 6.52, 55.75, 39.90, 34.05, 48.86],
    "lon":        [-74.01, -0.13, 139.69, 151.21, 72.88, -46.63,
                   31.23, 3.38, 37.62, 116.40, -118.24, 2.35],
    "population": [8_336_817, 9_002_488, 13_960_000, 5_312_000, 20_667_656,
                   12_325_232, 20_076_000, 14_800_000, 12_506_468,
                   21_542_000, 3_979_576, 2_161_000],
})
cities["radius"] = (cities["population"] / cities["population"].max()) * radius
cities["color_r"] = 167
cities["color_g"] = 139
cities["color_b"] = 250

# ── Layers ────────────────────────────────────────────────────────────────────
scatter = pdk.Layer(
    "ScatterplotLayer",
    data=cities,
    get_position=["lon", "lat"],
    get_radius="radius",
    get_fill_color=["color_r", "color_g", "color_b", int(opacity_val * 255)],
    pickable=True,
)
layers = [scatter]

if show_hex:
    # random points around cities for hexbin
    np.random.seed(0)
    pts = pd.DataFrame({
        "lon": np.random.uniform(-180, 180, 2000),
        "lat": np.random.uniform(-70, 70, 2000),
    })
    hex_layer = pdk.Layer(
        "HexagonLayer",
        data=pts,
        get_position=["lon", "lat"],
        radius=200_000,
        elevation_scale=5000,
        elevation_range=[0, 1000],
        pickable=True,
        extruded=True,
        coverage=0.8,
        color_range=[
            [1, 152, 189], [73, 227, 206], [216, 254, 181],
            [254, 237, 177], [254, 173, 84], [209, 55, 78],
        ],
    )
    layers.append(hex_layer)

view = pdk.ViewState(latitude=20, longitude=10, zoom=1.5, pitch=40 if show_hex else 0)

r = pdk.Deck(
    layers=layers,
    initial_view_state=view,
    tooltip={"text": "{city}\nPop: {population}"},
    map_style=f"mapbox://styles/mapbox/{map_style}-v10",
)
st.pydeck_chart(r)

# ── Table ─────────────────────────────────────────────────────────────────────
st.markdown("#### City Data")
st.dataframe(
    cities[["city", "lat", "lon", "population"]]
    .sort_values("population", ascending=False)
    .reset_index(drop=True),
    use_container_width=True,
)
