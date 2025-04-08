from sqlalchemy import select

from webchat.common.database.database import new_session, ChatOrm
from webchat.common.models import Message, MessageAdd


class ChatRepository():
    @classmethod
    async def add(cls, data: MessageAdd) -> int:
        async with new_session() as session:
            message_dict = data.model_dump()

            message = ChatOrm(**message_dict)
            session.add(message)
            # Получает данные из коммита без коммита
            await session.flush()
            await session.commit()
            return message.id

    @classmethod
    async def find_all(cls) -> list[Message]:
        async with new_session() as session:
            query = select(ChatOrm)
            result = await session.execute(query)
            message_models = result.scalars().all()
            print(repr(message_models))
            message_schemas = [Message.model_validate(message_model) for message_model in message_models]
            return message_schemas
