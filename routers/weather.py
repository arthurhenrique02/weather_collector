from fastapi import APIRouter
from fastapi.responses import JSONResponse

blueprint = "weather"

router = APIRouter(
    prefix=f"/{blueprint}",
    tags=[blueprint],
    responses={404: {"message": "Not Found"}},
)


@router.get("/today")
async def get_today_weather():
    """
    Get today's weather data.
    """
    # Placeholder for actual weather data retrieval logic
    return {"date": "2023-10-01", "temperature": "20°C", "condition": "Sunny"}