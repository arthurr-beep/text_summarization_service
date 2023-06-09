from fastapi import APIRouter, BackgroundTasks, HTTPException

from app.repository import summary_repo
from app.schemas.payload import SummaryPayload, SummaryResponse
from app.models.tortoise import SummarySchema
from typing import List
from app.utils.summarizer import generate_summary


router = APIRouter()


@router.post("/", response_model=SummaryResponse, status_code=201)
async def create_summary(payload: SummaryPayload, background_tasks: BackgroundTasks) -> SummaryResponse:
    summary_id = await summary_repo.post(payload)

    background_tasks.add_task(generate_summary, summary_id, payload.url)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object

@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await summary_repo.get(id)

    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await summary_repo.get_all()