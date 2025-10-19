# NutriTrack – AI-Powered Nutrition Tracker

NutriTrack is a terminal-based nutrition tracker that allows users to describe their meals in natural language and receive **calories and macronutrients** calculated via the **Edamam Nutrition Analysis API**.

Technologies used:

* **Python 3.11+**
* **Requests** for API calls
* **dotenv** for environment variables
* **FastAPI** (planned for web version)
* **Docker** (optional, for containerized deployment)

---

## Features

* Terminal chat interface to input meals
* Supports input like: `200g rice, 100g chicken, 2 eggs, banana`
* Automatically calculates **calories, protein, carbs, and fat**
* Uses Edamam API for reliable nutritional values
* Handles pieces and grams
* Stores optional history in `data/history.log`

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/NutriTrack.git
cd NutriTrack
```


### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Generate the `.env` file

Create a `.env` file at the project root. Use this template:

```env
API_NAME=edamam
API_URL=https://api.edamam.com/api/nutrition-data
API_ID=your_edamam_app_id
API_KEY=your_edamam_app_key
DEFAULT_PORTION_G=100
DEFAULT_PORTION_P=1
HISTORY_PATH=data/history.log
```

* Replace `your_edamam_app_id` and `your_edamam_app_key` with your credentials from [Edamam Developer Portal](https://developer.edamam.com/).


### 4. Run the terminal version

```bash
python main.py
```

* Example input:

```
200g rice, 100g chicken, 2 eggs, banana
```

* Press `h` for help
* Press `q` to quit

---



### 5. Notes

* Edamam API expects **English names** and precise formats: `<quantity><unit> <food>`

  * e.g., `100g rice`, `2 eggs`, `banana`
* Pieces are automatically handled.

---



### Future Improvements

* Full **FastAPI backend** + web interface
* Persistent user accounts
* Image recognition for food intake (PyTorch model)

---
