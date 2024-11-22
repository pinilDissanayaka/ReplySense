from langgraph.graph import StateGraph, END, START
from .nodes import Nodes
from .state import State





class Graph(object):
    def __init__(self):
        self.node=Nodes()


    def get_graph(self):
        work_flow=StateGraph(State)

        work_flow.add_node("check_emails", self.node.check_emails)
        work_flow.add_node("filter_emails", self.node.filter_emails)
        work_flow.add_node("report_emails", self.node.report_emails)
        #work_flow.add_node("wait", self.node.wait)
        work_flow.add_node("draft_writer", self.node.write_draft)



        work_flow.set_entry_point("check_emails")


        work_flow.add_edge("check_emails", "filter_emails")

        work_flow.add_conditional_edges(
        "filter_emails",
        self.node.decider,
        {
            "wait": "check_emails",
            "continue": "report_emails"
        }
        )
        work_flow.add_edge("report_emails", "draft_writer")
        work_flow.add_edge("draft_writer", END)
        #work_flow.add_edge("wait", "check_emails")


        graph=work_flow.compile()
        
        return graph
