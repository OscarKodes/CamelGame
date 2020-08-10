# Camel Game
import random
import time

# Greet Player ==========================================================
print("""
Welcome to Camel!

You have stolen a camel to make your way across the great Mobi desert.

The natives want their camel back and are chasing you down!

Survive your desert trek and outrun the natives.
""")

# Assign Variables ====================================================

menu = """
================================
A. Drink from your canteen.
B. Ahead moderate speed.
C. Ahead full speed.
D. Stop and rest.
E. Status check.
Q. Quit.
================================
What do you do? Enter a letter:
"""

milesTraveled = 0
thirst = 0
camelFatigue = 0
camelAlive = True
natives = -100
canteen = 3

# Define Game Functions ===================================================
def reactToPlayer():
    
    global milesTraveled, thirst, camelFatigue, natives, canteen
    
    if userChoice == "A":
        
        if canteen > 0:
            canteen -= 1
            thirst = 0
            print("You drink from the canteen. You feel refreshed.")
        else:
            print("Your canteen is empty. There is nothing to drink.")
            
    elif userChoice == "B":
        
        if camelAlive:
            
            milesTraveled += random.randint(6, 14)
            thirst += 1
            camelFatigue += 1
            
        else:
            
            milesTraveled += random.randint(2, 7)
            thirst += 2
        
        natives += random.randint(6, 14)
        print("You have traveled a total of %s miles." % milesTraveled)
        
    elif userChoice == "C":
                
        if camelAlive:
            
            milesTraveled += random.randint(12, 35)
            thirst += 1
            camelFatigue += random.randint(2, 4)
            
        else:
            
            milesTraveled += random.randint(3, 10)
            thirst += 3
        
        natives += random.randint(6, 14)
        print("You have traveled a total of %s miles." % milesTraveled)
        
    elif userChoice == "D":
        
        camelFatigue = 0
        natives += random.randint(6, 14)
        print("The camel is well rested.")
    
    elif userChoice == "E":
        
        print("""Miles traveled: %s
Drinks in canteen: %s
The natives are %s miles behind you.""" % (milesTraveled, canteen, -1 * natives))

def endGameCheck():
    
    if userChoice == "Q":
        return True
    
    if thirst > 6:
        print("\nYou have died of dehydration!")
        return True
        
    elif -1 * natives <= 0:
        print("\nThe natives have caught up to you and captured you.")
        return True
    
    elif milesTraveled >= 200:
        
        print("\nYou made it across the desert!\n\nCongratulations!")
        return True
    
    return False
    
def playerWarning():
    
    global camelAlive
    
    if -1 * natives < 15:
        
        print("\nThe natives are getting close!")
        
    if thirst > 4:
        
        print("\nYou are thirsty.")
        
    if camelAlive and camelFatigue > 8:
        
        camelAlive = False
        print("\nYour camel has died from being overworked.")
        print("\nYou are now running on foot.")
        
    elif camelAlive and camelFatigue > 5:
        
        print("\nYour camel is getting tired.")
        
def specialEvents():
    
    if random.randint(0, 20) == 0:
        
        global thirst, camelFatigue, canteen
        
        print("You found an oasis!")
        print("You quench your thirst and refill your canteen with the fresh oasis water.")
        canteen = 3
        thirst = 0
        
        if camelAlive:
            camelFatigue = 0
            print("Your camel is well rested.")
    
# Game Main Loop =========================================================
while True:
    
    print(menu)    # Shows the menu
    userChoice = input().upper()    # Gets user input
    print()
    
    # Reaction to user's input
    reactToPlayer()
    
    # Checks to see if any conditions have been met to end the game
    if endGameCheck():
        print("\nThank you for playing.")
        break
    
    # Checks if there are any warnings for the player
    playerWarning()
    
    # Special Events
    if userChoice not in "AE":
        specialEvents()
    
    # Pauses for 1 second
    time.sleep(1)
