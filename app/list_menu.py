from models.model_menu_list import Meal
from data import data

meals = data['meals']

def modify_ingredients(meals):
    ingredients = []
    for meal in meals:
        ingredient = meal['ingredients']
        for material in ingredient:
            ingredients.append(material['name'])
        meal['ingredients'] = ingredients
        ingredients=[]
 
modify_ingredients(meals)

food = []

for meal in meals:
    menu_item = Meal(
        id=meal['id'],
        name=meal['name'],
        ingredients=meal['ingredients']
    )
    food.append({menu_item})
    
print(food)
