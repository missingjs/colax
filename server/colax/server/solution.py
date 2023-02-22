from pydantic import BaseModel


class UserSolution(BaseModel):
    project: str
    language: str
    test_data: str
    source_code: str
