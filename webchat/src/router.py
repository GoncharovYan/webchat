from fastapi import APIRouter, Depends
from typing import Annotated

from webchat.common.database import ChatRepository
from webchat.common.models import Message, MessageAdd, MessageId

router = APIRouter(
    prefix="/messages",
    tags=["Сообщения"]
)


@router.get("")
async def get_messages() -> list[Message]:
    messages = await ChatRepository.find_all()
    return messages


@router.post("")
async def send_message(
        message: Annotated[MessageAdd, Depends()]
) -> MessageId:
    message_id = await ChatRepository.add(message)
    return MessageId(
        status=200,
        message_id=message_id
    )
