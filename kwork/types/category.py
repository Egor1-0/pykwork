from pydantic import BaseModel, field_validator


class Subcategory(BaseModel):
    id: int = 0
    name: str = ''
    description: str | None = None


class Category(BaseModel):
    id: int = 0
    name: str = ''
    description: str | None = ''
    subcategories: list[Subcategory] | None = None

    @field_validator('subcategories', mode='before')
    @classmethod
    def normalize_subcategories(cls, subcategories):
        if subcategories is None:
            return None

        return [Subcategory(**dict_category) for dict_category in subcategories]
