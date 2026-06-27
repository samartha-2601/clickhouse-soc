from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():

    return {
        "status": "ok",
        "application": "ClickHouse SOC",
        "version": "0.4.0"
    }