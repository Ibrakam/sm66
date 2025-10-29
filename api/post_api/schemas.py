from pydantic import BaseModel
from typing import Union


class PostSchema(BaseModel):
    title: str
    main_text: str
    uid: int


class PostRead(BaseModel):
    status: int
    message: Union[str | int | bool | list | dict]
