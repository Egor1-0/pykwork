from typing import Callable

from pydantic import BaseModel


class Handler(BaseModel):
    func: Callable
    text: str | None = None
    on_start: bool = False
    text_contains: str | None = None