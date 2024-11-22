from langgraph.graph import StateGraph, END, START
from .nodes import Nodes
from .state import State




node=Nodes()



work_flow=StateGraph(State)

work_flow.add_node("check_emails", node.check_emails)
work_flow.add_node("filter_emails", node.filter_emails)
work_flow.add_node("report_emails", node.report_emails)
work_flow.add_node("wait", node.wait)
work_flow.add_node("draft_writer", node.write_draft)



work_flow.set_entry_point("check_emails")


work_flow.add_edge("check_emails", "filter_emails")

work_flow.add_conditional_edges(
   "filter_emails",
   node.decider,
   {
       "wait": "wait",
       "continue": "report_emails"
   }
)
work_flow.add_edge("report_emails", "draft_writer")
work_flow.add_edge("draft_writer", "wait")
work_flow.add_edge("wait", "check_emails")


app=work_flow.compile()
