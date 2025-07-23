# Simple Chatbot with Memory using LangChain

A lightweight chatbot powered by LLMs with memory capabilities using Langchain and an interactive user interface built with Streamlit.

### Example Screenshot
![Simple Chatbot UI](https://github.com/canonflow/2025-master-langchain-and-ollama/blob/main/ASSETS/chatbot-ui-1.png?raw=true)

## 🚀 Features
- **Conversational Memory**: The bot remembers previous interactions per session.
- **Character Persona**: The assistant responds in the style of Jarvis.
- **Streamlit UI**: Clean and responsive chat interface.
- **Session Persistence**: Conversation history is saved to a database using `session_id`.
- **Multi-user Ready**: Designed to handle multiple users/sessions.


## 💻 Tech Stack
- LangChain
- Streamlit
- Ollama with Llama3.2:3B
- SQLite
- Python 3.11

## 📦 Installation
1. Clone the repository
```
git clone https://github.com/canonflow/2025-master-langchain-and-ollama
cd "07. Build Your Own Chatbot"
```
2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Copy .env.example to .env and add the necessary keys
```
cp .env.example .env
```
5. Pull Llama3.2:latest
```
ollama pull llama3.2:latest
```
6. Run the app
```
streamlit runn chat_stream.py
```

## 💡 How It Works
- Uses Langchain's RunnableWithMessageHistory to store and retrieve message history.
- Message data is stored in a SQL database (SQLite by default, but can be replaced with PostgreSQL or MySQL).
- The Streamlit interface handles input and real-time message streaming.
- System prompts can be customized to give the chatbot a unique personality (e.g., "You are Jarvis...").