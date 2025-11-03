import requests
from config import API_URL, API_ID, API_KEY

if not API_ID or not API_KEY:
    raise ValueError("Please set your API_ID and API_KEY in the .env file")



def get_nutrition (items: list[dict])->list[dict]:
    result = []
    for item in items :
        item_string = build_item_string(item=item)
        data = query(item_string)
        if data and ("parsed" in data and len(data["parsed"]) > 0):
            result.append(parse_nutrition_data(item_string,data))
    return result


def build_item_string (item:dict)-> str:
    quantity = item["quantity"]
    unit = item["unit"]
    product = item["product"]
    
    if unit == "piece":
        return f"{quantity} {product}"
    else:
        return f"{quantity}{unit} {product}"
    
def query(text : str) -> dict :
    params={
        "app_id" : API_ID,
        "app_key" : API_KEY,
        "ingr": text,
    }
    response = requests.get(API_URL,params=params,timeout=5)
    response.raise_for_status()
    return response.json()

def parse_nutrition_data(name: str, data : dict)-> dict:
    nutrients = data['ingredients'][0]['parsed'][0]['nutrients']
    calories=nutrients.get("ENERC_KCAL", {}).get("quantity", 0)
    protein = nutrients.get("PROCNT", {}).get("quantity", 0)
    carbs = nutrients.get("CHOCDF", {}).get("quantity", 0)
    fat = nutrients.get("FAT", {}).get("quantity", 0)

    return {
        "ingredient":  name,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat
    }
    
    
    
