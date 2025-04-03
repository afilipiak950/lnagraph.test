from typing import Sequence, TypedDict
from langgraph.graph import StateGraph
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import logging

# Konfiguriere Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Lade die Umgebungsvariablen
load_dotenv()

# Überprüfe API-Key
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY nicht gefunden in .env Datei")
logger.info("API-Key gefunden")

# Definiere den Zustandstyp
class AgentState(TypedDict):
    messages: Sequence[HumanMessage | AIMessage]
    next: str

# Erstelle einen einfachen Agenten
def create_agent():
    logger.info("Erstelle Agenten...")
    # Initialisiere das LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Definiere die Agenten-Logik
    def agent(state: AgentState):
        messages = state["messages"]
        logger.info(f"Verarbeite Nachricht: {messages[-1].content}")
        response = llm.invoke(messages)
        logger.info(f"Erhielt Antwort: {response.content}")
        return {"messages": [*messages, response], "next": "end"}
    
    # Definiere den End-Knoten
    def end(state: AgentState):
        return state
    
    # Erstelle den Workflow
    workflow = StateGraph(AgentState)
    
    # Füge die Knoten hinzu
    workflow.add_node("agent", agent)
    workflow.add_node("end", end)
    
    # Setze den Startpunkt
    workflow.set_entry_point("agent")
    
    # Füge die Kante hinzu
    workflow.add_edge("agent", "end")
    
    return workflow.compile()

# Beispiel für die Verwendung
if __name__ == "__main__":
    try:
        # Erstelle den Agenten
        agent = create_agent()
        
        # Erstelle den initialen Zustand
        initial_state = {
            "messages": [HumanMessage(content="Was ist die Hauptstadt von Deutschland?")],
            "next": "agent"
        }
        
        # Führe den Agenten aus
        logger.info("Starte Agenten-Ausführung...")
        result = agent.invoke(initial_state)
        
        # Gib die Antwort aus
        logger.info("Antworten:")
        for message in result["messages"]:
            print(f"{message.type}: {message.content}")
            
    except Exception as e:
        logger.error(f"Fehler bei der Ausführung: {str(e)}")
        raise 