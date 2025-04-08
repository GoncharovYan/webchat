from pydantic import BaseModel, ConfigDict


class MessageAdd(BaseModel):
    # author_id: int
    text: str


class Message(MessageAdd):
    model_config = ConfigDict(from_attributes=True)
    id: int


class MessageId(BaseModel):
    status: int
    message_id: int
