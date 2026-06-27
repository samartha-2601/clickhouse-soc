from fastapi import APIRouter

from backend.incident_engine.engine import IncidentEngine

router = APIRouter(
    prefix="/correlate",
    tags=["Incidents"],
)


@router.post("")
def correlate():

    engine = IncidentEngine()

    engine.run()

    return {
        "status": "completed",
        "message": "Incident correlation completed."
    }