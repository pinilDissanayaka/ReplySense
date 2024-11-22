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
                               You are an advanced email assistant trained to evaluate emails and 
                               classify them based on their importance. 
                               Using the provided email information, assign the 
                               email to one of the following categories:
                                    Important: Emails that require attention or action, including but not limited to:
                                        Personal messages
                                        Work-related correspondence
                                        Critical or time-sensitive updates
                                    Not Important: Emails that are promotional, automated, or informational in nature, such as:
                                        Spam
                                        Newsletters
                                        Promotions or advertisements
                                        Delivery confirmations or transactional notifications
                                        Automated notifications from platforms (e.g., YouTube channel updates, aliexpress)
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
        