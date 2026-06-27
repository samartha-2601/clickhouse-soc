from fastapi import APIRouter

from backend.detection_engine.engine import DetectionEngine

router = APIRouter(
    prefix="/detect",
    tags=["Detection"],
)


@router.post("")
def detect():

    engine = DetectionEngine()

    engine.run()

    return {
        "status": "completed",
        "message": "Detection engine finished."
    }