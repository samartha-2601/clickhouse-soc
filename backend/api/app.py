from fastapi import FastAPI

from backend.api.routers.health import router as health_router
from backend.api.routers.events import router as events_router
from backend.api.routers.alerts import router as alerts_router
from backend.api.routers.incidents import router as incidents_router
from backend.api.routers.simulator import router as simulator_router
from backend.api.routers.detection import router as detection_router
from backend.api.routers.correlation import router as correlation_router

app = FastAPI(

    title="ClickHouse SOC",

    description="AI-powered Detection Engineering and Incident Response Platform",

    version="0.4.0",
)

app.include_router(health_router)
app.include_router(events_router)
app.include_router(alerts_router)
app.include_router(incidents_router)
app.include_router(simulator_router)
app.include_router(detection_router)
app.include_router(correlation_router)