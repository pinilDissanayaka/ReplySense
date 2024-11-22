import os
import time
from .state import State
from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.search import GmailSearch
from .agents import EmailAnalyst
from .agents import EmailDrafter



class Nodes(object):
    def __init__(self):
        self.tool_kit = GmailToolkit()
        self.search_condition="is:unread label:inbox"
        
    
    def check_emails(self, state: State):
        gmail_search_tool=GmailSearch(api_resource=self.tool_kit.api_resource)
        
        emails=gmail_search_tool.invoke(self.search_condition)
        
        email_ids=[]
        unread_emails= state["email_ids"] if state["email_ids"] else []
        
        for email in emails:
            if email["id"] not in email_ids:
                unread_emails.append({
                    "id":email["id"],
                    "threadId":email["threadId"],
                    "sender":email["sender"],
                    "date":email["date"],
                    "subject":email["subject"],
                    "body":email["body"],
                    "snippet":email["snippet"]
                })
                
                email_ids.append(email["id"])
        
        return{
            "unread_emails":unread_emails,
            "email_ids":email_ids
        }
        
    
    def filter_emails(self, state: State):
        emails=state["unread_emails"]
        action_required_emails=[]
        
        for email in emails:
            category=EmailAnalyst().invoke(sender=email["sender"], subject=email["subject"], email=email["body"])

            if category == "Important":
                action_required_emails.append({
                    "id":email["id"],
                    "threadId":email["threadId"],
                    "sender":email["sender"],
                    "date":email["date"],
                    "subject":email["subject"],
                    "body":email["body"],
                    "snippet":email["snippet"]
                })
                
        return{
            ** state,
            "action_required_emails":action_required_emails,
            "emails":emails
        }
    
    
    def decider(self, state: State):
        emails=state["action_required_emails"]
        
        if len(emails) == 0:
            return "wait"
        else:
            return "continue"
            
            
    def wait(self, state: State):
        time.sleep(2)
        
        print("wait")
        
        return{
            ** state
        }

    def report_emails(self, state: State):
        emails=state["action_required_emails"]
        for idx, email in enumerate(emails):
            with open("important_emails.md", "a", encoding="utf-8") as md_file: 
                md_file.write(f"Email {idx+1}\n" + "-"*150 + "\n")
                md_file.write(f"Date: {email['date']}")
                md_file.write(f"Id: {email['id']}")
                md_file.write(f"Sender: {email['sender']}")
                md_file.write(f"Subject: {email['subject']}")
                md_file.write(f"Body: {email['body']}")
                md_file.write("-"*150 + "\n")
                
        return {
            ** state
        }
        
    def write_draft(self, state: State):
        emails=state["action_required_emails"]
        
        for idx, email in enumerate(emails):
            EmailDrafter().invoke(email=email["body"], subject=email["subject"], sender=email["sender"])
            emails.pop(idx)
            
        return{
            ** state,
            "action_required_emails":emails
        }