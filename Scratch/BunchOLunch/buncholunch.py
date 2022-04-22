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
    ''' 
    1. Choose random dish from foodWeLike - Done!
    2. Check dish hasn't been chosen. If not add to myMenu. - Done!
    3. Repeat until we have required number of dishes in myMenu. - Done!
    '''

#A2. Build shopping list


#B. -------------Lists---------------

foodWeLike = ["Pizza", "Beef Burgers", "Pork Stir Fry", "Chicken Fajitas", "Bangers n Mash", "Fish n Chips", "Spanish Omelette"]

myMenu = []

#1. How many days to plan?

print("Hello I'm Bunch! I'll help you plan your dinner menu...")
answer = input("How many days would you like me to plan? ")
print("OK, I'm going to plan " + answer + " dinner(s) from your favourite meal list.")

#2. Choose dishes

chooseDishes(answer)
print("Done! Here's your menu...")
print()
print(myMenu)
print()
print("Out of all these dishes, my favourite has to be..." + choice(myMenu))

#3. Build shopping list