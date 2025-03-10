from pydantic import BaseModel, Field

from kwork.types.message import LastMessage


class Notify:
    NEW_MESSAGE = "new_message"

#ENUMS
class EventType:
    IS_TYPING = "is_typing"
    NOTIFY = "notify"
    NEW_MESSAGE = "new_inbox"
    POP_UP_NOTIFY = "pop_up_notify"
    MESSAGE_DELETE = "inbox_message_delete"
    REMOVE_POP_UP_NOTIFY = "remove_pop_up_notify"
    DIALOG_UPDATE = "dialog_updated"


class EventData(BaseModel):
    from_user_id: int = Field(alias='from')
    message_text: str = Field(alias='inboxMessage')
    to_user_id: int
    conversation_id: int
    title: str | None = ''
    last_message: LastMessage | None = None
    event_type: EventType | None = Field(None, alias='eventType')
    is_custom_request: bool = Field(alias='isCustomRequest')
    is_yescrow: bool = Field(alias='is_yescrow')
    push_queue_id: int | None = Field(0, alias='pushQueueId')


class BaseEvent(BaseModel):
    event: str | None = ''
    data: EventData | None = None
