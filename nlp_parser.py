
from curses.ascii import isalnum
from config import DEFAULT_PORTION_P, DEFAULT_PORTION_G


def normalize (text: str )-> str :
    normalized_s= ""
    for char in text :
         if (isalnum(char) or char ==" " or char ==","):
             normalized_s +=char.lower()
    return normalized_s

def extract_quantities(text : str)-> dict:
    text=text.strip()
    quantity="" 
    unit=""

    i = 0
    while i < len(text) and text[i].isdigit():
        quantity += text[i]
        i += 1
        
    while i < len(text) and text[i].isalpha():
        unit += text[i]
        i += 1
        
    if (i ==len(text)):   #Case where no unit nor quantity is written (only one piece of ingredient)
        i-=len(unit)
        unit=""
        
    if unit == "":
        unit = "piece"    

    if quantity == "":
        if unit == "piece" :
            quantity = DEFAULT_PORTION_P
        else : 
            quantity = DEFAULT_PORTION_G
    else : 
        quantity = int(quantity)    
        
    
    return {"quantity" : quantity, "unit": unit , "product": text[i:].strip()}      
            
def parse (text: str) -> list[dict]:
    text = normalize(text)
    tokens = [t.strip() for t in text.split(",")]
    result = []
    for token in tokens:
        if token:
            result.append(extract_quantities(token))
    return result
         
    
        
            
        
            
                