import os
import streamlit as st
from src.graph import Graph


def run_graph():
    Graph().get_graph().invoke({"email_ids":[]})


st.set_page_config(page_title="ReplySense", page_icon=":robot_face:")

with st.sidebar:
    generation=st.button("Generate Reply")
    
    if generation:
        if "generation" not in st.session_state or "generation" in st.session_state:
            with st.spinner("Generating Reply..."):
                run_graph()
                st.session_state.generation=True
                st.success("Reply Generated")
    else:
        if "generation" not in st.session_state or "generation" in st.session_state:
            st.session_state.generation=False
            
    if os.path.exists("important_emails.md"):
        if st.button("Delete Important Emails"):
            os.remove("important_emails.md")
    


st.title('Email Reply Automation')


if "generation" in st.session_state:
    if st.session_state.generation:
        with st.expander("Unread Important Emails", expanded=False):
            if os.path.exists("important_emails.md"):
                with open("important_emails.md", "r", encoding="utf-8") as md_file:
                    st.markdown(md_file.read())
        


