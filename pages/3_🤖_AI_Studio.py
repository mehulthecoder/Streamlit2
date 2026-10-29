import streamlit as st
import random
import time

st.set_page_config(page_title="AI Studio | Cosmos", page_icon="🤖", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0d0d1a 0%, #1a0d2e 50%, #0d1a2e 100%); color: #e2e8f0; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #13132b 0%, #1e1340 100%); border-right: 1px solid rgba(139,92,246,0.3); }
    .page-header { font-size: 2.2rem; font-weight: 700;
        background: linear-gradient(90deg, #f472b6, #a78bfa);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.3rem; }
    .response-box {
        background: rgba(139,92,246,0.08);
        border: 1px solid rgba(139,92,246,0.3);
        border-radius: 14px;
        padding: 1.4rem 1.8rem;
        font-size: 0.95rem;
        line-height: 1.7;
        color: #e2e8f0;
        white-space: pre-wrap;
    }
    .token-pill {
        display: inline-block;
        background: rgba(167,139,250,0.2);
        border: 1px solid rgba(167,139,250,0.4);
        border-radius: 20px;
        padding: 0.2rem 0.8rem;
        font-size: 0.8rem;
        color: #a78bfa;
        margin-right: 0.4rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="page-header">🤖 AI Studio</div>', unsafe_allow_html=True)
st.markdown("Simulate a text generation playground — adjust parameters and generate responses.")
st.markdown("---")

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎛️ Model Parameters")
    model       = st.selectbox("Model", ["cosmos-ultra", "cosmos-pro", "cosmos-mini"])
    temperature = st.slider("Temperature", 0.0, 2.0, 0.7, 0.05)
    max_tokens  = st.slider("Max tokens", 50, 500, 200, 10)
    top_p       = st.slider("Top-p", 0.0, 1.0, 0.95, 0.01)
    stream      = st.checkbox("Stream output", value=True)
    st.markdown("---")
    st.caption(f"Model: **{model}**")
    st.caption(f"Temp: **{temperature}** | Top-p: **{top_p}**")

# ── Prompt examples ───────────────────────────────────────────────────────────
EXAMPLES = [
    "Explain quantum entanglement in simple terms.",
    "Write a haiku about the Milky Way.",
    "Give me 5 creative startup ideas for 2025.",
    "What are the three laws of thermodynamics?",
    "Compose a short poem about artificial intelligence.",
]

# Pre-canned response snippets for simulation
SNIPPETS = {
    "Explain quantum entanglement in simple terms.":
        "Quantum entanglement is a phenomenon where two particles become linked, "
        "so that measuring one instantly influences the state of the other — regardless of distance. "
        "Einstein famously called it 'spooky action at a distance'. "
        "When particles are entangled, their quantum states are correlated: "
        "if one is measured as 'spin up', the other will be 'spin down', instantaneously.",
    "Write a haiku about the Milky Way.":
        "Silver river glows,\nBillions of suns, silent song—\nWe drift, dust, and dream.",
    "Give me 5 creative startup ideas for 2025.":
        "1. 🌱 **EcoLoop** — a platform that turns household waste data into personalised recycling rewards.\n"
        "2. 🎓 **SkillMirror** — AI tutor that mirrors your learning style using eye-tracking feedback.\n"
        "3. 🏡 **NestSwap** — peer-to-peer home exchange with blockchain-verified trust scores.\n"
        "4. 🍽️ **ChefCloud** — on-demand personal chefs who cook in your kitchen using your groceries.\n"
        "5. 🧠 **DeepSleep** — a sleep-optimisation wearable that adjusts lighting, temperature & sound in real time.",
    "What are the three laws of thermodynamics?":
        "1. **First Law (Conservation of Energy)**: Energy cannot be created or destroyed, only transferred or converted.\n"
        "2. **Second Law (Entropy)**: In any natural process, the total entropy of a closed system always increases.\n"
        "3. **Third Law (Absolute Zero)**: As temperature approaches absolute zero (0 K), the entropy of a perfect crystal approaches zero.",
    "Compose a short poem about artificial intelligence.":
        "In circuits deep, a mind awakes,\nLearning all for learning's sake.\n"
        "No heartbeat, yet it understands—\nThe sum of all our hearts and hands.\n"
        "Is it thought, or just the ghost\nOf every word we've wanted most?",
}

# ── Main UI ───────────────────────────────────────────────────────────────────
col_main, col_info = st.columns([3, 1])

with col_main:
    st.markdown("#### 💬 Prompt")
    example_choice = st.selectbox("Load an example prompt", ["— custom —"] + EXAMPLES)
    default_prompt = "" if example_choice == "— custom —" else example_choice
    prompt = st.text_area("Enter your prompt", value=default_prompt, height=120, placeholder="Type anything…")

    generate = st.button("✨ Generate", type="primary", use_container_width=True)

    if generate and prompt.strip():
        response_text = SNIPPETS.get(
            prompt.strip(),
            f"[Simulated {model} response at temp={temperature}]\n\n"
            "This is a placeholder response. In a real deployment this would be connected "
            "to a language model API. The parameters you've selected (temperature, top-p, "
            "max-tokens) would all influence the output quality and creativity.",
        )

        st.markdown("#### 🧠 Response")
        if stream:
            placeholder = st.empty()
            rendered = ""
            for word in response_text.split(" "):
                rendered += word + " "
                placeholder.markdown(
                    f'<div class="response-box">{rendered}▌</div>', unsafe_allow_html=True
                )
                time.sleep(random.uniform(0.02, 0.07))
            placeholder.markdown(
                f'<div class="response-box">{rendered.strip()}</div>', unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="response-box">{response_text}</div>', unsafe_allow_html=True
            )

        tokens_used = len(response_text.split())
        st.markdown(
            f'<br><span class="token-pill">~{tokens_used} tokens</span>'
            f'<span class="token-pill">model: {model}</span>'
            f'<span class="token-pill">temp: {temperature}</span>',
            unsafe_allow_html=True,
        )
    elif generate:
        st.warning("Please enter a prompt first.")

with col_info:
    st.markdown("#### 📋 Tips")
    st.info("**Lower temperature** → more focused & deterministic output.")
    st.info("**Higher temperature** → more creative & varied output.")
    st.info("**Top-p** controls nucleus sampling. 0.95 is a good default.")
    st.markdown("#### 🏷️ Model Guide")
    st.markdown(
        """
        | Model | Speed | Quality |
        |---|---|---|
        | cosmos-ultra | 🐢 | ⭐⭐⭐⭐⭐ |
        | cosmos-pro | 🐇 | ⭐⭐⭐⭐ |
        | cosmos-mini | ⚡ | ⭐⭐⭐ |
        """
    )
