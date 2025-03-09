from pydantic import BaseModel, Field


class PortfolioItem(BaseModel):
    id: int = 0
    title: str = ''
    order_id: int = 0
    category_id: int = 0
    category_name: str = ''
    item_type: str = Field('', alias="type")
    photo: str = ''
    video: str = ''
    views: int = 0
    views_dirty: int = 0
    comments_count: int = 0
    images: list[dict] | None = None
    videos: list[dict] | None = None
    audios: list[dict] | None = None
    pdf: list[dict] | None = None
    duplicate_from: str = ''
    pined_at_timestamp: int = 0