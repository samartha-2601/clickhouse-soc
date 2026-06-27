from fastapi import APIRouter

from backend.database.alert_repository import AlertRepository

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)

repo = AlertRepository()


@router.get("")
def get_alerts(limit: int = 100):

    return repo.get_recent_alerts(limit)