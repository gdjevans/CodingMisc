'''
Bunch O Lunch App

The purpose of Bunch O Lunch is to produce a dinner menu from favourite dishes, and produce a shopping list of the ingredients if required. 
'''
# ---- Imports ----
from random import choice


#A. -------------Functions--------------

#A1.  Choose dishes

def chooseDishes(days): 
    while len(myMenu) < int(days):
        chosenDish = choice(foodWeLike)
        if chosenDish not in myMenu:
            myMenu.append(chosenDish)
    print("Done! Here's your menu...")
    print()
    for dish in myMenu:
        print(dish)
    print()
    print("Out of all these dishes, my favourite has to be..." + choice(myMenu))
    ''' 
    1. Choose random dish from foodWeLike - Done!
    2. Check dish hasn't been chosen. If not add to myMenu. - Done!
    3. Repeat until we have required number of dishes in myMenu. - Done!
    '''

#A2. Build shopping list

def buildShoppingList():
    myShoppingList = []
    if "Pizza" in myMenu:
        myShoppingList.append(pizza)
    if "Beef Burgers" in myMenu:
        myShoppingList.append(beefBurgers)
    if "Pork Stir Fry" in myMenu:
        myShoppingList.append(stirFry)
    if "Chicken Fajitas" in myMenu:
        myShoppingList.append(chickenFajitas)
    if "Bangers n Mash" in myMenu:
        myShoppingList.append(bangersNMash)
    if "Fish n Chips" in myMenu:
        myShoppingList.append(fishNChips)
    if "Spanish Omelette" in myMenu:
        myShoppingList.append(spanishOmelette)
    for dish in myShoppingList:
        for ingredient in dish:
            print(ingredient)
    print("Voila! Bon apetit!")
    


#B. -------------Lists---------------

foodWeLike = ["Pizza", "Beef Burgers", "Pork Stir Fry", "Chicken Fajitas", "Bangers n Mash", "Fish n Chips", "Spanish Omelette"]

pizza = ["Dough base", "Tomato Sauce", "Cheese", "Peperroni", "Peppers"]
beefBurgers = ["Beef", "Rolls", "Lettuce", "Tomatoes", "Relish"]
stirFry = ["Pork", "Peppers", "Onion", "Hoi Sin Sauce", "Egg Noodles"]
chickenFajitas = ["Chicken", "Red Peppers", "Onion", "Flour Wrap", "Chilli Sauce"]
bangersNMash = ["Sausages", "Potatoes", "Gravy", "Onion", "Peas"]
fishNChips = ["Cod", "Potatoes", "Tartar Sauce", "Peas"]
spanishOmelette =["Eggs", "Chorizo", "Potatoes", "Chicken", "Onion"]

myMenu = []

#1. How many days to plan?

print("Hello I'm Bunch! I'll help you plan your dinner menu...")
answer = input("How many days would you like me to plan? ")
print("OK, I'm going to plan " + answer + " dinner(s) from your favourite meal list.")

#2. Choose dishes

chooseDishes(answer)


#3. Build shopping list

answer = input("Would you like a shopping list for this menu? ")

if answer == 'y':
    buildShoppingList()
else:
    print()
    print("You got it! Bye for now...")