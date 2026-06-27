from fastapi import APIRouter, HTTPException

from backend.database.incident_repository import IncidentRepository
from backend.investigation_engine.engine import InvestigationEngine

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"],
)

repo = IncidentRepository()

engine = InvestigationEngine()


@router.get("")
def get_incidents(limit: int = 100):

    return repo.get_recent_incidents(limit)


@router.post("/{incident_id}/investigate")
def investigate_incident(
    incident_id: str,
):

    investigation = engine.investigate(
        incident_id,
    )

    if investigation is None:

        raise HTTPException(
            status_code=404,
            detail="Incident not found",
        )

    return investigation