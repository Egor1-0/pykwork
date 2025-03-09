from pydantic import BaseModel

from kwork.types.achievement import Achievement
from kwork.types.kwork_object import KworkObject
from kwork.types.portfolio import PortfolioItem
from kwork.types.review import Review


class User(BaseModel):
    id: int
    username: str
    status: str
    fullname: str
    profilepicture: str
    description: str = ''
    slogan: str = ''
    location: str = ''
    rating: float = 0.0
    rating_count: int = 0
    level_description: str = ''
    good_reviews: int = 0
    bad_reviews: int = 0
    online: bool
    live_date: int
    cover: str = ''
    custom_request_min_budget: int = 0
    is_allow_custom_request: int = 0
    order_done_persent: int = 0
    order_done_intime_persent: int = 0
    order_done_repeat_persent: int = 0
    timezoneId: int
    blocked_by_user: bool
    allowedDialog: bool
    addtime: int
    achievments_list: list[Achievement] | None = None
    completed_orders_count: int = 0
    specialization: str | None = None
    profession: str | None = None
    kworks_count: int
    kworks: list[KworkObject] | None = None
    portfolio_list: list[PortfolioItem] | None = None
    reviews: list[Review] | None = None
