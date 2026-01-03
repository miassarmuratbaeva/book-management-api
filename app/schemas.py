from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    year: int
    rating: float = Field(ge=0.0, le=5.0)

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BookBase):
    id: int

    class Config:
        orm_mode = True
