from pydantic import BaseModel


class SampleJobParam(BaseModel):
    name: str
    age: int
