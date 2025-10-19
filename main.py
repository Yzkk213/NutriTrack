
from nutrition_api import get_nutrition
from nlp_parser import parse

def main ():
    
    print(
    "\nWelcome to NutriTrack! Describe your meal and we'll calculate the macros.\n\n"
    "Please follow this input pattern:\n\n"
    "  'Quantity' + 'Unit' (if applicable) + 'space' + 'product'\n\n"
    "- To add multiple products, separate them with a ',' comma.\n"
    "- If you have a single product without quantity/unit, just type its name (e.g., 'banana').\n"
    "- Quantities without a specified unit will default to grams for foods, or 'piece' for items like eggs or fruits.\n\n"
    "Example: 200g rice, 100g chicken, 2 eggs, banana\n\n"
    "Press 'h' for help.\n"
    )


    while True:
        user_input = input("> ")
        
        match user_input : 
            case "q" : 
                print ("Goodbye")
                break
            case "h" : 
                print(      
                    "Describe your meal like this : '200g rice, 2 eggs'.\n"
                    "Commands:\n"
                    "  q - quit\n"
                    "  h - help\n"
                )
                
            case _ : 
                list_ingredients = parse(user_input)
                list_macros = get_nutrition(list_ingredients)

                sum_protein = 0
                sum_cals = 0
                sum_carbs = 0
                sum_fats = 0

                print("\nNutrition breakdown per item:")
                for i, (ingredient, macros) in enumerate(zip(list_ingredients, list_macros), 1):
                    name = macros["ingredient"]
                    calories = macros["calories"]
                    protein = macros["protein"]
                    carbs = macros["carbs"]
                    fat = macros["fat"]

                    print(f"{i}. {name}: {calories:.1f} kcal, {protein:.1f}g protein, {carbs:.1f}g carbs, {fat:.1f}g fat")

                    # Add to total intake
                    sum_cals += calories
                    sum_protein += protein
                    sum_carbs += carbs
                    sum_fats += fat

                print("\nTotal intake:")
                print(f"Calories: {sum_cals:.1f} kcal, Protein: {sum_protein:.1f}g, Carbs: {sum_carbs:.1f}g, Fat: {sum_fats:.1f}g")

           
            
if __name__ == "__main__":
    main()