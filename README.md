# LangGraph Chat App

Eine interaktive Chat-Anwendung, die LangGraph und Streamlit verwendet, um einen intelligenten Chatbot zu erstellen.

## Features

- 🤖 Interaktives Chat-Interface
- 💬 Persistenter Chat-Verlauf
- ⚡ Echtzeit-Antworten
- 🔄 Zustandsverwaltung mit LangGraph

## Installation

1. Klonen Sie das Repository:
```bash
git clone https://github.com/afilipiak950/langgraph-chat.git
cd langgraph-chat
```

2. Installieren Sie die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

3. Erstellen Sie eine `.env`-Datei mit Ihrem OpenAI API-Schlüssel:
```
OPENAI_API_KEY=your-api-key-here
```

## Verwendung

Starten Sie die App lokal:
```bash
streamlit run app.py
```

Die App ist dann unter http://localhost:8501 verfügbar.

## Deployment

Die App kann einfach auf Streamlit Cloud deployed werden:

1. Erstellen Sie ein Konto auf [Streamlit Cloud](https://streamlit.io/cloud)
2. Verbinden Sie Ihr GitHub-Repository
3. Wählen Sie die `app.py` als Hauptdatei
4. Fügen Sie Ihre Umgebungsvariablen hinzu
5. Deploy!

## Lizenz

MIT 