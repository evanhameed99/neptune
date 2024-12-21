from pydantic import BaseModel


class CompletionPayload(BaseModel):
    session_id: str
    prompt: str
