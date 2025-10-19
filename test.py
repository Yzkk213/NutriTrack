import requests
from config import API_URL, API_ID, API_KEY
from nutrition_api import get_nutrition
from nlp_parser import parse

params = {
    "app_id": API_ID,
    "app_key": API_KEY,
    "ingr": "100g rice"
}

import requests
import json

resp = requests.get(API_URL, params=params)

# Convert response to JSON
data = resp.json()  # this parses the response body as JSON

# Pretty print
print(json.dumps(data, indent=4))


