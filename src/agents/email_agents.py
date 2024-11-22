from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from ..llm import llm
from pydantic import BaseModel, Field
from typing import Literal

class Email(BaseModel):
    category: Literal["Important", "Not Important"]

class EmailAnalyst(object):
    def __init__(self):
        self.llm=llm
        self.structured_llm=llm.with_structured_output(Email)
    
    def invoke(self, subject, sender, email):
        message=[SystemMessage(content="""
                               You are given an email text. Your task is to determine whether the email contains both personal and work-related content.
                               If the email is both personal and work-related, then you should respond with "Important". Otherwise, you should respond with "Not Important".
                               """),
                 
                 HumanMessage(content="""
                                sender: {SENDER}
                                Subject : {SUBJECT}
                                Email : {EMAIL}
                              """)]
        
        prompt=ChatPromptTemplate.from_messages(message)
        
        chain=(
            {"SENDER" : RunnablePassthrough(), "SUBJECT" : RunnablePassthrough(), "EMAIL" : RunnablePassthrough()} |
            prompt |
            self.structured_llm
        )
        
        result = chain.invoke({"SENDER" : sender, "SUBJECT" : subject, "EMAIL" : email})
        
        return result.category
        