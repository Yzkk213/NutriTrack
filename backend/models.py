from pydantic import BaseModel, Field
from typing import List, Optional

class MacroData(BaseModel):
    calories: float
    protein: float
    carbs: float
    fat: float

class Meal(BaseModel):
    id: Optional[str] = Field(default=None, alias="_id")
    meal_name: Optional[str] = None
    user_id: str
    items: str  
    macros: Optional[MacroData] = None