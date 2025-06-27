from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from langchain.chat_models import ChatOpenAI
from tools.flight import book_flight
from tools.hotel import book_hotel
from tools.calendar import block_calendar_event

def build_travel_graph():
    llm = ChatOpenAI(model="gpt-4o")

    def extract_intent(state):
        text = state["input"]
        # Naively extract details; replace with proper parsing
        return {
            "departure": "DXB",
            "destination": "LHR",
            "date": "2025-07-10",
            "check_in": "2025-07-10",
            "check_out": "2025-07-15",
            "time": "09:00 AM"
        }

    def call_flight(state):
        details = state["details"]
        state["flight"] = book_flight(details["departure"], details["destination"], details["date"])
        return state

    def call_hotel(state):
        details = state["details"]
        state["hotel"] = book_hotel(details["destination"], details["check_in"], details["check_out"])
        return state

    def call_calendar(state):
        details = state["details"]
        event = f"Trip to {details['destination']}"
        state["calendar"] = block_calendar_event(event, details["date"], details["time"], "Flight + Hotel booked")
        return state

    # State structure
    class TravelState(dict):
        pass

    graph = StateGraph(TravelState)
    graph.add_node("parse", extract_intent)
    graph.add_node("book_flight", call_flight)
    graph.add_node("book_hotel", call_hotel)
    graph.add_node("block_calendar", call_calendar)

    # Connect nodes
    graph.set_entry_point("parse")
    graph.add_edge("parse", "book_flight")
    graph.add_edge("book_flight", "book_hotel")
    graph.add_edge("book_hotel", "block_calendar")

    graph.set_finish_point("block_calendar")

    return graph.compile()
