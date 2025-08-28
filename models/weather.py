from pydantic import BaseModel
from typing import Optional

class WeatherStation(BaseModel):
    station_id: str
    prefecture: str
    location: str
    current_value: float
    
    class Config:
        from_attributes = True