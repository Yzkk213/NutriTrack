from dotenv import load_dotenv
import os 


load_dotenv()

API_NAME = os.getenv("API_NAME", "edamam")
API_URL = os.getenv("API_URL", "")
API_KEY = os.getenv("API_KEY", "")
API_ID = os.getenv("API_ID","")
DEFAULT_PORTION_G = int(os.getenv("DEFAULT_PORTION_G", 100))
DEFAULT_PORTION_P= int(os.getenv("DEFAULT_PORTION_P", 1))
HISTORY_PATH = "data/history.log"
