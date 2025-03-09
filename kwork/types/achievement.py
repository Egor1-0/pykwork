from pydantic import BaseModel


class Achievement(BaseModel):
    id: int = 0
    name: str = ''
    description: str = ''
    image_url: str = ''
