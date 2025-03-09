from pydantic import BaseModel


class KworkMinObject(BaseModel):
    id: int = 0
    title: str = ''
    active: int = 0
    feat: bool


class Writer(BaseModel):
    id: int = 0
    username: str = ''
    profilepicture: str = ''


class Review(BaseModel):
    id: int = 0
    time_added: int = 0
    text: str = ''
    auto_mode: str | None = None
    good: bool
    bad: bool
    kwork: KworkMinObject
    writer: Writer
