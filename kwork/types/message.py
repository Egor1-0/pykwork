import asyncio

from pydantic import BaseModel


class InboxMessage(BaseModel):
    message_id: int = 0
    to_id: int = 0
    to_username: str | None = None
    to_live_date: int = 0
    from_id: int = 0
    from_username: str | None = None
    from_live_date: int = 0
    from_profilepicture: str | None = None
    to_profilepicture: str | None = None
    manager_name: str | None = ''
    message: str | None = ''
    time: int = 0
    unread: bool
    type: str | None = None
    status: str | None = None
    created_order_id: int | None = 0
    forwarded: bool
    updated_at: int | None = 0
    warning_type: str | None = None
    countup: int = 0
    conversation_id: int = 0
    message_page: int = 0


class Message:
    def __init__(
            self,
            api,
            from_id: int,
            text: str,
            to_user_id: int = 0,
            inbox_id: int = 0,
            last_message: dict | None = None,
            title: str | None = '',
    ):
        self.api = api
        self.from_id = from_id
        self.text = text
        self.to_user_id = to_user_id
        self.inbox_id = inbox_id
        self.title = title
        self.last_message = last_message

    async def answer_simulation(self, text: str):
        """
        realistic answer with typing simulation and waiting
        :param text:
        :return:
        """
        await asyncio.sleep(2)
        await self.api.set_typing(self.from_id)
        await asyncio.sleep(len(text) // 4)
        await self.api.send_message(self.from_id, text=text)

    async def fast_answer(self, text: str):
        await self.api.send_message(self.from_id, text=text)
