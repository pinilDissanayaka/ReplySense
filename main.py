from src.graph import Graph


def run():
    graph=Graph().get_graph()

    graph.invoke({"email_ids":[]})
