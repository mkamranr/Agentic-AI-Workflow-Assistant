from graph.travel_graph import build_travel_graph

if __name__ == "__main__":
    graph = build_travel_graph()
    result = graph.invoke({"input": "Book my flight from Dubai to London on July 10 and hotel for 5 days"})
    print("Result:", result)
