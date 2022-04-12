from pydantic import BaseModel


class Job(BaseModel):
    title: str
    description: str
    employer: str
    location: str


class JobModel(Job):
    id: int
