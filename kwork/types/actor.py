from pydantic import BaseModel, Field

from kwork.types.achievement import Achievement
from kwork.types.kwork_object import KworkObject
from kwork.types.portfolio import PortfolioItem
from kwork.types.review import Review


class Actor(BaseModel):
    id: int
    username: str
    status: str
    email: str
    type: str
    verified: bool
    profile_picture: str = Field(default='', alias='profilepicture')
    description: str = ''
    slogan: str = ''
    fullname: str = ''
    level_description: str = ''
    cover: str = ''
    good_reviews: int
    bad_reviews: int
    location: str = ''
    rating: float = 0.0
    rating_count: int = 0
    total_amount: int = 0
    hold_amount: int = 0
    free_amount: int = 0
    currency: str = ''
    inbox_archive_count: int = 0
    unread_dialog_count: int = 0
    notify_unread_count: int = 0
    red_notify: bool
    warning_inbox_count: int = 0
    app_notify_count: int = 0
    unread_messages_count: int = 0
    fullname_en: str = Field('', alias="fullnameEn")
    description_en: str = Field('', alias="descriptionEn")
    country_id: int = 0
    city_id: int = 0
    timezone_id: int = 0
    addtime: int = 0
    allow_mobile_push: bool
    is_more_payer: bool
    kworks_count: int = 0
    favourite_kworks_count: int = 0
    hidden_kworks_count: int = 0
    specialization: str = ''
    profession: str = ''
    kworks_available_at_weekends: bool
    achievments_list: list[Achievement] | None = None
    completed_orders_count: int = 0
    kworks: list[KworkObject] = None
    portfolio_list: list[PortfolioItem] | None = None
    reviews: list[Review] | None = None
    worker_status: str = None
    has_offers: bool
    wants_count: int = 0
    offers_count: int = 0
    archived_wants_count: int = 0
    push_notifications_sound_allowed: bool = Field(
        alias="pushNotificationsSoundAllowed"
    )
    black_friday_for_sellers: bool = None