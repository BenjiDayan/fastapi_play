from sql import Field, SQLModel
from typing import Optional

class Quote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    quote: str
    author: str
    author_extra: Optional[str] = None

