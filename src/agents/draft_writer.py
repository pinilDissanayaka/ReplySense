from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from ..llm import llm
from pydantic import BaseModel, Field
from typing import Literal
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.create_draft import GmailCreateDraft


class EmailDraft(BaseModel):
    subject: str = Field(description="The subject of the email draft.")
    body: str = Field(description="The body of the email draft.")


class EmailDrafter(object):
    def __init__(self):
        self.tool_kit = GmailToolkit()
        self.llm=llm
        self.structured_llm=llm.with_structured_output(EmailDraft)
        self.gmail_create_draft=GmailCreateDraft(api_resource=self.tool_kit.api_resource)
        
    def invoke(self, email: str, subject: str, sender):
        prompt_template="""
            You are an advanced email assistant trained to compose professional, clear, and 
            context-appropriate email drafts. Using the provided details, craft an email that is concise, 
            polite, and suited to the given purpose.
                Instructions:
                    Carefully review the recipient(s), subject, and key details provided.
                    Use a tone that matches the context, such as formal, semi-formal, or casual.
            Write a professional email draft based on the following details
                subject: {SUBJECT}
                email: {EMAIL}
        """
        
        prompt=ChatPromptTemplate.from_template(prompt_template)
        
        chain=(
            {"EMAIL": RunnablePassthrough(), "SUBJECT": RunnablePassthrough()} |
            prompt |
            self.structured_llm
        )
        
        response=chain.invoke({"EMAIL": email, "SUBJECT": subject})
        
        
        self.gmail_create_draft.invoke({
            'to': [sender],
			'subject': response.subject,
			'message': response.body
        })
        
    