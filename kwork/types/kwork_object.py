from pydantic import BaseModel, Field


class Cover(BaseModel):
    phone: str = None
    tablet: str = None


class Worker(BaseModel):
    id: int = 0
    username: str = ''
    fullname: str = ''
    profilepicture: str = ''
    rating: float = 0.0
    reviews_count: int = 0
    rating_count: int = 0
    is_online: bool


class Activity(BaseModel):
    views: int = 0
    orders: int = 0
    earned: int = 0


class KworkObject(BaseModel):
    id: int = 0
    category_id: int = 0
    category_name: str = ''
    status_id: int = 0
    status_name: str = ''
    title: str = ''
    url: str = ''
    image_url: str = ''
    cover: Cover | None = None
    price: int = 0
    is_price_from: bool
    is_from: bool
    photo: str = ''
    is_best: bool
    is_hidden: bool
    is_favorite: bool
    lang: str = ''
    worker: Worker = None
    activity: Activity = None
    edits_list: list | None = None
    profile_sort: int = 0
    is_subscription: bool = Field(alias="isSubscription")
