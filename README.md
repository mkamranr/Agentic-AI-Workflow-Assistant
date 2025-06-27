# 🧠 Agentic AI Workflow Assistant (Multi-Step Planner)

This project implements a multi-step **LLM Agent** using **LangGraph** that can understand and complete complex user requests like:

> "Book my flight from Dubai to London, reserve a hotel, and block time in my calendar."

## 🛠 Features

- ✅ Intent extraction from natural language
- ✈️ Flight booking (mocked)
- 🏨 Hotel booking (mocked)
- 📅 Calendar blocking (mocked via Google Calendar)
- 🔁 Multi-step orchestration with LangGraph

---

## 📂 Project Structure

```
agentic-assistant/
├── main.py                    # Entry point to run the graph
├── tools/
│   ├── flight.py              # Mock flight booking
│   ├── hotel.py               # Mock hotel booking
│   └── calendar.py           # Mock calendar event
├── graph/
│   └── travel_graph.py        # LangGraph flow logic
├── config.py                  # Environment/config management
├── .env                       # Store API keys (excluded from repo)
└── requirements.txt           # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/agentic-assistant.git
cd agentic-assistant
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Setup API Keys

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your-openai-api-key
```

> 📌 This project uses `ChatOpenAI` from LangChain with GPT-4o. You can switch to Claude or others if needed.

---

## ▶️ Running the Assistant

Use the following command:

```bash
python main.py
```

It will process the input:
```
"Book my flight from Dubai to London on July 10 and hotel for 5 days"
```

Expected output:

```json
{
  "flight": {
    "flight_number": "SKY123",
    "departure": "DXB",
    "arrival": "LHR",
    "date": "2025-07-10",
    "booking_id": "FLIGHT-001"
  },
  "hotel": {
    "hotel_name": "City Inn",
    "location": "LHR",
    "check_in": "2025-07-10",
    "check_out": "2025-07-15",
    "booking_id": "HOTEL-002"
  },
  "calendar": {
    "event_id": "CAL-003",
    "status": "confirmed"
  }
}
```

---

## 📌 Notes

- All API calls are currently **mocked**. You can replace them with real integrations:
  - [Amadeus for Flights](https://developers.amadeus.com/)
  - [Booking.com or Expedia](https://developers.expediagroup.com/)
  - [Google Calendar API](https://developers.google.com/calendar)

- The current version uses hardcoded values for simplicity. For production, integrate entity extraction (e.g., LangChain tools, structured output parsers, or Pydantic schemas).

---

## 🧩 Roadmap

- [ ] Add real API integrations
- [ ] Add natural language parsing (e.g., date and location from text)
- [ ] Implement fallback/error handling
- [ ] Add user memory and profiles

---

## 🧠 Built With

- [LangGraph](https://docs.langgraph.dev)
- [LangChain](https://www.langchain.com/)
- [OpenAI GPT-4o](https://openai.com/gpt-4o)

---

## 👨‍💻 Author

Muhammad Kamran Rafi  
[GitHub](https://github.com/mkamranr) • [LinkedIn](https://www.linkedin.com/in/kamranrafi/)
