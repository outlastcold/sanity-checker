from pydantic import BaseModel
from datetime import date

class Load(BaseModel):
    origin: str
    destination: str
    miles: int
    customer_rate: float
    carrier_rate: float
    equipment: str
    weight: int
    pickup_date: date
    delivery_date: date
    commodity: str
    new_carrier: bool
    carrier_mc_age_days: int