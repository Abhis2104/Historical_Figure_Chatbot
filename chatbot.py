"""chatbot.py – Groq API integration with streaming and error handling."""

from groq import Groq, APIStatusError, APIConnectionError, AuthenticationError, RateLimitError
from config import GROQ_API_KEY, GROQ_MODEL


def get_client() -> Groq:
    return Groq(api_key=GROQ_API_KEY)


def _build_messages(system_prompt: str, conversation_history: list[dict], user_message: str) -> list[dict]:
    messages = [{"role": "system", "content": system_prompt}]
    for turn in conversation_history:
        role = "assistant" if turn["role"] == "model" else turn["role"]
        messages.append({"role": role, "content": turn["text"]})
    messages.append({"role": "user", "content": user_message})
    return messages


def generate_response_stream(
    system_prompt: str,
    conversation_history: list[dict],
    user_message: str,
):
    """
    Yields text chunks as they stream from Groq.
    Use with st.write_stream() in Streamlit.
    """
    client = get_client()
    messages = _build_messages(system_prompt, conversation_history, user_message)

    try:
        stream = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=messages,
            temperature=0.5,
            max_tokens=300,
            stream=True,
        )
        for chunk in stream:
            text = chunk.choices[0].delta.content
            if text:
                yield text

    except AuthenticationError:
        raise Exception("AUTH_ERROR")
    except RateLimitError:
        raise Exception("RATE_LIMIT")
    except APIConnectionError:
        raise Exception("NETWORK_ERROR")
    except APIStatusError as e:
        raise Exception(str(e))
