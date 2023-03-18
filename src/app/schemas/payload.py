from pydantic import BaseModel


class SummaryPayload(BaseModel):
    url: str


class SummaryResponse(SummaryPayload):
    id: int