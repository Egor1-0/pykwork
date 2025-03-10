import asyncio
import json
import logging
from urllib.parse import unquote

import websockets

from kwork import KworkClient
from kwork.exceptions import KworkException
from kwork.types import BaseEvent, EventType, Message, Notify, Dialog, InboxMessage
from kwork.types.handler import Handler


class Dispatcher:
    client: KworkClient
    # _routers: list[Router]
    _handlers: list[Handler] = []

    def __init__(self, client: KworkClient):
        self.client = client

    async def listen_messages(self):
        channel = await self.client.get_channel()
        uri = f"wss://notice.kwork.ru/ws/public/{channel}"
        while True:
            try:
                async with websockets.connect(uri) as websocket:
                    try:
                        data = await websocket.recv()
                    except websockets.exceptions.ConnectionClosedError as e:
                        logging.debug(f"Get {e}, reboot socket...")
                        continue
                    logging.debug(f"Get updates from websocket - {data}")


                    json_event = json.loads(data)

                    json_event['text'] = unquote(json_event['text'])
                    json_event_data = json.loads(json_event["text"])

                    event: BaseEvent = BaseEvent(**json_event_data)

                    if event.event is not EventType.NEW_MESSAGE:
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
                            dialogs_page = await self.client.api_request(
                                method="post",
                                api_method="dialogs",
                                filter="all",
                                page=1,
                                token=await self.client.token,
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
                                await self.client.get_dialog_with_user(
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
                            await self.client.get_dialog_with_user(
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

            except Exception as e:
                logging.error(f"Get error in polling - {e}, restarting")
                await asyncio.sleep(10)

    async def run_bot(self):
        async for message in self.listen_messages():
            print('new message', message)