import asyncio
import json
import logging
import urllib.parse
from typing import List, Optional, Callable

import aiohttp
import websockets

from ..types import Actor, User, Connects, Category, Dialog, InboxMessage, Order, BaseEvent, EventType, Message, Notify
from kwork.exceptions import KworkException, KworkBotException
from ..types.handler import Handler

logger = logging.getLogger(__name__)

class KworkBot(Kwork):
    def __init__(self, login: str, password: str, proxy: str = None):
        super().__init__(login, password, proxy)
        self._handlers: List[Handler] = []

    async def listen_messages(self):
        logger.info("Starting listen messages")
        while True:
            try:
                channel = await self._get_channel()
                uri = f"wss://notice.kwork.ru/ws/public/{channel}"
                async with websockets.connect(uri) as websocket:
                    try:
                        data = await websocket.recv()
                    except websockets.exceptions.ConnectionClosedError as e:
                        logging.debug(f"Get {e}, reboot socket...")
                        continue

                    logging.debug(f"Get updates from websocket - {data}")

                    json_event = json.loads(data)
                    json_event_data = json.loads(json_event["text"])

                    event: BaseEvent = BaseEvent(**json_event_data)
                    if event.event in [EventType.IS_TYPING]:
                        continue

                    if event.event == EventType.NEW_MESSAGE:
                        message: Message = Message(
                            api=self,
                            from_id=event.data["from"],
                            text=event.data["inboxMessage"],
                            to_user_id=event.data["to_user_id"],
                            inbox_id=event.data["inbox_id"],
                            title=event.data["title"],
                            last_message=event.data["lastMessage"],
                        )
                        yield message
                    elif (
                            event.event == EventType.NOTIFY
                            and event.data.get(Notify.NEW_MESSAGE) is not None
                    ):
                        if event.data.get("dialog_data") is None:
                            dialogs_page = await self.api_request(
                                method="post",
                                api_method="dialogs",
                                filter="all",
                                page=1,
                                token=await self.token,
                            )
                            last_dialog = Dialog(**dialogs_page["response"][0])

                            from_id, text, to_user_id, inbox_id = (
                                last_dialog.user_id,
                                last_dialog.last_message,
                                None,
                                None,
                            )
                        else:
                            # TODO: вынести логику
                            message_raw: InboxMessage = (
                                await self.get_dialog_with_user(
                                    event.data["dialog_data"][0]["login"]
                                )
                            )[0]

                            from_id, text, to_user_id, inbox_id = (
                                message_raw.from_id,
                                message_raw.message,
                                message_raw.to_id,
                                message_raw.message_id,
                            )
                        message: Message = Message(
                            api=self,
                            from_id=from_id,
                            text=text,
                            to_user_id=to_user_id,
                            inbox_id=inbox_id,
                        )
                        yield message

                    elif event.event == EventType.POP_UP_NOTIFY:
                        message_raw: InboxMessage = (
                            await self.get_dialog_with_user(
                                event.data["pop_up_notify"]["data"]["username"]
                            )
                        )[0]
                        message: Message = Message(
                            api=self,
                            from_id=message_raw.from_id,
                            text=message_raw.message,
                            to_user_id=message_raw.to_id,
                            inbox_id=message_raw.message_id,
                        )
                        yield message
            except KworkException as e:
                logging.error(f"Get error in polling - {e}, restarting")
                await asyncio.sleep(10)

    @staticmethod
    def _dispatch_text_contains(text, message_text) -> bool:
        lower_text = [word.lower() for word in message_text.split()]
        for word in lower_text:
            if text == word.strip("...").strip("!").strip(".").strip("?").strip("-"):
                return True
        return False

    async def _dispatch_message(
            self, message: Message, handler: Handler
    ) -> Optional[Callable]:
        if not any([handler.on_start, handler.text, handler.text_contains]):
            return handler.func

        if handler.on_start:
            from_username = (await self.get_all_dialogs())[0].username
            current_dialog = await self.get_dialog_with_user(from_username)
            if len(current_dialog) == 1:
                return handler.func
        elif (
                handler is not None
                and handler.text is not None
                and handler.text.lower() == message.text.lower()
        ):
            return handler.func
        elif handler.text_contains is not None and self._dispatch_text_contains(
                handler.text_contains, message.text
        ):
            return handler.func
        return None

    def message_handler(
            self, text: str = None, on_start: bool = False, text_contains: str = None
    ):
        """
        :param text: answer on exact match of message
        :param on_start: answer only on fist message in dialog
        :param text_contains: answer if message contains this text
        :return:
        """

        def decorator(func: Callable) -> Callable:
            handler = Handler(func, text, on_start, text_contains)
            self._handlers.append(handler)
            return func

        return decorator

    async def run_bot(self):
        if not self._handlers:
            raise KworkBotException("You have to create handler")
        logging.info("Bot is running!")
        async for message in self.listen_messages():
            for handler in self._handlers:
                handler_func = await self._dispatch_message(message, handler)
                logger.debug(f"Found handler - {handler_func}")
                if handler_func is not None:
                    await handler_func(message)
