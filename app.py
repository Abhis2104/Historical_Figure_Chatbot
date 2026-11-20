"""app.py – Streamlit interface and application flow."""

import streamlit as st
from config import validate_api_key, GROQ_MODEL
from personas import PERSONAS, PERSONA_NAMES
from chatbot import generate_response_stream

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Historical Figure Persona Chatbot",
    page_icon="🏛️",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    .disclaimer-banner {
        background: #fff3cd;
        border: 2px solid #ffc107;
        border-radius: 8px;
        padding: 10px 16px;
        font-weight: 600;
        color: #856404;
        margin-bottom: 12px;
        font-size: 0.95rem;
    }
    .persona-header {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
        color: white;
        padding: 14px 20px;
        border-radius: 10px;
        margin-bottom: 16px;
        font-size: 1.2rem;
        font-weight: 700;
    }
    .suggested-q {
        font-size: 0.85rem;
        color: #555;
        margin-bottom: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Session state initialisation ──────────────────────────────────────────────
if "selected_persona" not in st.session_state:
    st.session_state.selected_persona = PERSONA_NAMES[0]
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []  # {"role": "user"/"assistant", "content": "..."}

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🏛️ Historical Figures")
    st.markdown("---")

    chosen = st.selectbox(
        "Select a Historical Figure",
        PERSONA_NAMES,
        index=PERSONA_NAMES.index(st.session_state.selected_persona),
    )

    # Reset conversation when persona changes
    if chosen != st.session_state.selected_persona:
        st.session_state.selected_persona = chosen
        st.session_state.conversation_history = []
        st.session_state.chat_messages = []
        st.rerun()

    persona = PERSONAS[chosen]

    st.markdown(f"### {persona['emoji']} {chosen}")
    st.caption(persona["years"])
    st.markdown("**Biography**")
    st.write(persona["bio"])

    st.markdown("**Key Achievements**")
    for ach in persona["achievements"]:
        st.markdown(f"- {ach}")

    st.markdown("**Personality**")
    st.info(persona["personality"])

    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.conversation_history = []
        st.session_state.chat_messages = []
        st.rerun()

    st.markdown("---")
    st.caption(f"Model: `{GROQ_MODEL}`")

# ── Main area ─────────────────────────────────────────────────────────────────
st.markdown(
    "<h1 style='text-align:center;'>🏛️ Historical Figure Persona Chatbot</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align:center; color:#666;'>Learn History Through Interactive AI Role-Play</p>",
    unsafe_allow_html=True,
)

# Disclaimer banner
st.markdown(
    "<div class='disclaimer-banner'>"
    "⚠️ AI ROLE-PLAY: This is an AI-generated simulation of a historical personality, "
    "not the actual person."
    "</div>",
    unsafe_allow_html=True,
)

# API key validation
api_ok, api_error = validate_api_key()
if not api_ok:
    st.error(f"🔑 API Key Error: {api_error}")
    st.info("Add your Gemini API key to the `.env` file:\n```\nGEMINI_API_KEY=your_key_here\n```")
    st.stop()

# Active persona header
persona = PERSONAS[st.session_state.selected_persona]
st.markdown(
    f"<div class='persona-header'>{persona['emoji']} Chatting with: {st.session_state.selected_persona}</div>",
    unsafe_allow_html=True,
)

# Welcome message (shown only when chat is empty)
if not st.session_state.chat_messages:
    with st.chat_message("assistant"):
        st.write(persona["welcome"])
    st.markdown("**💡 Suggested Questions:**")
    cols = st.columns(2)
    for i, q in enumerate(persona["suggested_questions"]):
        cols[i % 2].markdown(f"<div class='suggested-q'>▶ {q}</div>", unsafe_allow_html=True)
    st.markdown("---")

# Render existing chat history
for msg in st.session_state.chat_messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input(f"Ask {st.session_state.selected_persona} a question…")

if user_input:
    stripped = user_input.strip()
    if not stripped:
        st.warning("Please enter a question.")
    else:
        # Display user message
        with st.chat_message("user"):
            st.write(stripped)
        st.session_state.chat_messages.append({"role": "user", "content": stripped})

        # Generate response
        with st.chat_message("assistant"):
            thinking = st.empty()
            thinking.markdown(f"*{persona['emoji']} {st.session_state.selected_persona} is thinking…*")
            try:
                stream = generate_response_stream(
                    system_prompt=persona["system_prompt"],
                    conversation_history=st.session_state.conversation_history,
                    user_message=stripped,
                )
                thinking.empty()  # clear the thinking message before streaming
                reply = st.write_stream(stream)
                st.session_state.conversation_history.append({"role": "user", "text": stripped})
                st.session_state.conversation_history.append({"role": "model", "text": reply})
                st.session_state.chat_messages.append({"role": "assistant", "content": reply})

            except Exception as exc:
                err_msg = str(exc)
                if "AUTH_ERROR" in err_msg:
                    st.error("🔑 Invalid or expired Groq API key. Please check your `.env` file.")
                elif "RATE_LIMIT" in err_msg:
                    st.error("⏳ Groq rate limit reached. Please wait a moment and try again.")
                elif "NETWORK_ERROR" in err_msg:
                    st.error("🌐 Network error. Please check your internet connection.")
                else:
                    st.error(f"❌ Something went wrong: {err_msg}")
