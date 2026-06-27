from fastapi import APIRouter

from backend.api.schemas.event import EventResponse
from backend.database.repository import EventRepository

router = APIRouter(
    prefix="/events",
    tags=["Events"],
)

repo = EventRepository()


@router.get(
    "",
    response_model=list[EventResponse],
)
def get_events(
    limit: int = 100,
    offset: int = 0,
    username: str | None = None,
    host: str | None = None,
    severity: str | None = None,
    event_type: str | None = None,
):

    return repo.get_events(
        limit=limit,
        offset=offset,
        username=username,
        host=host,
        severity=severity,
        event_type=event_type,
    )