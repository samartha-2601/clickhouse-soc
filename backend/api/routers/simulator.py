from fastapi import APIRouter

from backend.run_simulator import main

router = APIRouter(
    prefix="/simulate",
    tags=["Simulator"],
)


@router.post("")
def simulate():

    main()

    return {
        "status": "completed",
        "message": "Simulation finished."
    }