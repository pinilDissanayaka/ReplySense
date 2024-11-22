from typing import TypedDict

class State(TypedDict):
    email_ids: list
    unread_emails: list
    action_required_emails: list
    draft_response: list
    x: str