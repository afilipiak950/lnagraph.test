import streamlit as st
from langgraph_example import create_agent
from langchain_core.messages import HumanMessage
import logging

# Konfiguriere Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialisiere den Agenten
@st.cache_resource
def get_agent():
    return create_agent()

# Initialisiere die Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Titel der App
st.title("🤖 LangGraph Chat")

# Chat-Verlauf anzeigen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat-Eingabe
if prompt := st.chat_input("Was möchten Sie wissen?"):
    # Füge die Benutzernachricht zum Chat-Verlauf hinzu
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Hole den Agenten
    agent = get_agent()
    
    # Erstelle den initialen Zustand
    initial_state = {
        "messages": [HumanMessage(content=prompt)],
        "next": "agent"
    }
    
    # Führe den Agenten aus
    with st.chat_message("assistant"):
        with st.spinner("Denke nach..."):
            result = agent.invoke(initial_state)
            response = result["messages"][-1].content
            st.markdown(response)
            
    # Füge die Antwort zum Chat-Verlauf hinzu
    st.session_state.messages.append({"role": "assistant", "content": response}) 