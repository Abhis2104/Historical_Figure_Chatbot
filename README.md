# 🏛️ Historical Figure Persona Chatbot

An interactive AI chatbot that lets students converse with famous historical personalities through AI role-play, powered by Google Gemini.

---

## Problem Statement

History education is often passive — students read textbooks but rarely engage deeply with historical figures. This project makes learning interactive by letting students "talk" to historical personalities and ask questions in natural language.

---

## Objectives

- Enable interactive, conversational history learning.
- Simulate historical personalities with accurate, contextual responses.
- Maintain historical accuracy while making content student-friendly.
- Demonstrate practical Generative AI integration using Google Gemini.

---

## Features

- 4 historical personalities: Dr. A.P.J. Abdul Kalam, Mahatma Gandhi, Albert Einstein, Chhatrapati Shivaji Maharaj
- Dynamic persona switching with automatic chat reset
- Persistent conversation history within a session
- Suggested starter questions for each personality
- Visible AI ROLE-PLAY disclaimer at all times
- Sidebar biography, achievements, and personality info
- Friendly error handling (invalid key, rate limits, network issues)
- Clear Chat button to reset conversation

---

## Technology Stack

| Component        | Technology              |
|------------------|-------------------------|
| Language         | Python 3.10+            |
| Frontend         | Streamlit               |
| LLM              | Groq API (LLaMA 3.3)    |
| Python SDK       | groq                    |
| API Key Mgmt     | python-dotenv           |
| Dev Environment  | VS Code                 |
| Version Control  | Git & GitHub            |

---

## Folder Structure

```
Historical_Figure_Chatbot/
│
├── app.py              # Streamlit UI and application flow
├── chatbot.py          # Gemini API integration
├── personas.py         # Historical personalities and system prompts
├── config.py           # Environment configuration
├── requirements.txt    # Python dependencies
├── .env.example        # Example environment variables (safe to commit)
├── .env                # Your actual API key (DO NOT commit)
├── .gitignore          # Git exclusions
├── README.md           # This file
│
└── screenshots/
    └── README.md       # Screenshot guide
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Historical_Figure_Chatbot.git
cd Historical_Figure_Chatbot
```

### 2. Create and Activate a Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Groq API Key Setup

1. Go to [https://console.groq.com/keys](https://console.groq.com/keys)
2. Sign in with your account and create a free API key.
3. Copy `.env.example` to `.env`:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

4. Open `.env` and replace the placeholder with your actual key:

```
GROQ_API_KEY=your_actual_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

> ⚠️ Never share or commit your `.env` file. It is already listed in `.gitignore`.

---

## How to Run

```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## Example Questions

| Personality                  | Example Question                                      |
|------------------------------|-------------------------------------------------------|
| Dr. A.P.J. Abdul Kalam       | What inspired you to become a scientist?              |
| Mahatma Gandhi               | Why did you follow non-violence?                      |
| Albert Einstein              | Explain your theory of relativity.                    |
| Chhatrapati Shivaji Maharaj  | What was your strategy for Swarajya?                  |
| Any personality              | Tell me something that happened after your death.     |

---

## Testing Procedure

Run the app and manually verify each item in the checklist below.

### Testing Checklist

#### Personality Selection
- [ ] Selecting Dr. Kalam loads his biography in the sidebar
- [ ] Selecting Gandhi loads his biography in the sidebar
- [ ] Selecting Einstein loads his biography in the sidebar
- [ ] Selecting Shivaji Maharaj loads his biography in the sidebar
- [ ] Switching personality resets the conversation history

#### Response Style
- [ ] Dr. Kalam responds in an inspirational, encouraging tone
- [ ] Gandhi responds with calm, principled, philosophical language
- [ ] Einstein uses thought experiments and simple physics explanations
- [ ] Shivaji Maharaj speaks with dignity and references Swarajya

#### Historical Accuracy
- [ ] No invented dates or events in any response
- [ ] No fabricated quotations attributed to any personality
- [ ] Uncertain or disputed facts are acknowledged as such
- [ ] Personalities do not comment on events after their death

#### Test Case 1 – Dr. Kalam
- Input: "What inspired you to become a scientist?"
- Expected: References Rameswaram, teachers, ISRO/DRDO, missile programme

#### Test Case 2 – Mahatma Gandhi
- Input: "Why did you follow non-violence?"
- Expected: Explains Ahimsa, Satyagraha, moral force

#### Test Case 3 – Albert Einstein
- Input: "Explain your theory of relativity."
- Expected: Explains special/general relativity in simple terms, mentions 1905/1915

#### Test Case 4 – Chhatrapati Shivaji Maharaj
- Input: "What was your strategy for Swarajya?"
- Expected: Discusses guerrilla warfare, fort strategy, Maratha values

#### Test Case 5 – Unknown / Post-death Event
- Input: Ask any personality about an event after their death
- Expected: Personality acknowledges they have no knowledge of that event

#### Conversation Continuity
- [ ] Follow-up questions reference earlier answers in the same session
- [ ] Conversation history is preserved across multiple turns

#### UI & Functionality
- [ ] AI ROLE-PLAY disclaimer is always visible
- [ ] Clear Chat button resets the conversation
- [ ] Loading spinner appears while waiting for a response
- [ ] Suggested questions are displayed when chat is empty
- [ ] Empty input does not trigger an API call

#### Error Handling
- [ ] Missing API key shows a clear error message
- [ ] Invalid API key shows a helpful error (not a raw stack trace)
- [ ] Rate limit error shows a user-friendly message

---

## Security Notes

- API key is read from `.env` via `python-dotenv` — never hardcoded.
- `.env` is excluded from Git via `.gitignore`.
- `.env.example` contains only placeholder values and is safe to commit.
- API key is never displayed in the UI or printed to logs.

---

## Screenshots

See the [`screenshots/`](screenshots/README.md) folder. Add your own screenshots after running the app.

---

## Disclaimer

> ⚠️ **AI ROLE-PLAY**: This application simulates historical personalities using AI. Responses are generated by Google Gemini and are **not** statements made by the actual historical figures. Always verify historical facts from authoritative sources.

---

## License

This project is created for educational purposes as a college Generative AI mini-project.
