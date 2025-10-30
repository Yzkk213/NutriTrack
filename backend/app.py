from fastapi import FastAPI
from backend.db import db, get_next_meal_number
from backend.id import generate_meal_id
from backend.models import Meal, MacroData
from nlp_parser import parse
from nutrition_api import get_nutrition 

meal_counter = 1
app = FastAPI(title="NutriTrack API")

@app.get("/")
def root():
    return {"message": "Welcome to NutriTrack API!"}



@app.post("/meals")
def add_meals(meal: Meal):

    list_ingredients = parse(meal.items)
    list_macros = get_nutrition(list_ingredients)
    sum_protein = 0
    sum_cals = 0
    sum_carbs = 0
    sum_fats = 0
    
    for macros in list_macros:
        sum_cals+= macros["calories"]
        sum_protein += macros["protein"]
        sum_carbs += macros["carbs"]
        sum_fats += macros["fat"]
        
    macro_dict = {
        "calories":  round(sum_cals,2),
        "protein": round(sum_protein,2),
        "carbs": round(sum_carbs,2),
        "fat": round(sum_fats,2)
    }
    
    if meal.id is None : 
        meal.id= generate_meal_id()
        
    if not meal.meal_name or meal.meal_name.strip() == "":
        i = get_next_meal_number()
        meal.meal_name = f"meal{i}"
   
    meal.macros=MacroData(**macro_dict)
    db["meals"].insert_one(meal.dict())
    return {"status": "success", "name":meal.meal_name,"meal": meal.dict()}

@app.get("/meals/{meal_name}")
def get_meal(meal_name: str):
    if not meal_name:
        return {"status": "failure"}

    meals = list(db["meals"].find())
    for meal in meals:
        if meal.get("meal_name") == meal_name:
            # convert ObjectId to string for JSON
            meal["_id"] = str(meal["_id"])
            return {"status": "success", "name": meal["meal_name"], "meal": meal}

    return {"status": "failure"}

    
@app.get("/meals")
def get_all_meals():
    meals = list(db["meals"].find())
    # convert all ObjectIds to strings
    for m in meals:
        m["_id"] = str(m["_id"])
    return {"status": "success", "meals": meals}

@app.delete("/meals/{meal_name}")
def delete_meal(meal_name: str):
    if not meal_name:
        return {"status": "failure", "message": "Meal name required"}
    
    result = db["meals"].delete_one({"meal_name": meal_name})
    
    if result.deleted_count == 0:
        return {"status": "failure", "message": f"No meal found with name '{meal_name}'"}
    
    return {"status": "success", "message": f"Meal '{meal_name}' deleted successfully"}

@app.delete("/meals")
def delete_all_meals():
    result = db["meals"].delete_many({})
    return {
        "status": "success",
        "deleted_count": result.deleted_count,
        "message": f"Deleted {result.deleted_count} meals from database."
    }


@app.put("/meals/{meal_name}")
def update_meal(meal_name: str, updated_data: dict):
    if not meal_name:
        return {"status": "failure", "message": "Meal name required"}
    
    # Prevent MongoDB _id overwrite if passed accidentally
    if "_id" in updated_data:
        del updated_data["_id"]
    
    result = db["meals"].update_one(
        {"meal_name": meal_name},
        {"$set": updated_data}
    )
    
    if result.matched_count == 0:
        return {"status": "failure", "message": f"No meal found with name '{meal_name}'"}
    
    # Fetch the updated meal to return it
    updated_meal = db["meals"].find_one({"meal_name": meal_name})
    updated_meal["_id"] = str(updated_meal["_id"])
    
    return {"status": "success", "updated_meal":updated_meal}


