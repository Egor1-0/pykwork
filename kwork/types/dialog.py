from pydantic import BaseModel, Field



class LastMessage(BaseModel):
    unread: bool
    fromUsername: str = ''
    fromUserId: int = 0
    message_type: str = Field(alias='type')
    time: int = 0
    message: str = ''


class Dialog(BaseModel):
    unread: bool
    unread_count: int = 0
    time: int = 0
    user_id: int = 0
    username: str | None = ''
    last_message_text: str | None = ''
    profile_picture: str | None = Field(None, alias='profilepicture')
    is_online: bool
    lastOnlineTime: int = 0
    link: str | None = ''
    status: str | None = ''
    blocked_by_user: bool
    allowed_dialog: bool = Field(alias='allowedDialog')
    last_message: LastMessage | None = Field(None, alias='lastMessage')
    has_active_order: bool
    archived: bool
    is_starred: bool = Field(0, alias='isStarred')
    warning_message_id: int = 0
    countup: int = 0
    has_answer: bool
    is_allow_custom_request: bool
    hidden_at: int = 0
    is_important: bool
    moderation_status: str | None = None
    draft: str | None = ''
    disallow_reason: int = Field(0, alias='disallowReason')
    active_orders: list[dict] | None = None
    not_available_for_company: bool