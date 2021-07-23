
def rollercoaster(height):
    bill = 0
    if height >= 120:
        print("You can ride the rollercoaster!")
        age = int(input("Enter you age: "))
        if age < 12:
            bill = 5
            print("Child tickets are $5 only")
        elif 12 <= age <= 18:
            bill = 7
            print("Young tickets are $7 only")
        elif 45 <= age <= 55:
            print("You got free Rollercoaster ride!")
        else:
            bill = 12
            print("Adult tickets $12")

        want_to_take_a_photo = input("Do you want a photo taken? Y or N. ")
        if want_to_take_a_photo == 'Y':
            bill += 3

        print(f"Your final bill is ${bill}")
    else:
        print("Sorry, you have to grow taller before you can ride")


def bmiCalculater():
    height = float(input("Enter your height in m: "))
    weight = float(input("Enter your weight in km: "))
    bmi = round(weight / (height ** 2))
    if weight < 18.5:
        msg = "Under Weight"
    elif 18.5 < weight < 25:
        msg = "normal Weight"
    elif 25 < weight < 30:
        msg = "Over Weight"
    elif 30 < weight < 35:
        msg = "obese"
    elif weight > 30:
        msg = "Clinically obese"
    print(f"Your BMI is {bmi}, you slightly {msg}")


def leapYear():
    year = int(input("Enter year: "))
    if year % 4 == 0:
        print("Leap Year")
    else:
        print("Not a Leap Year")
        


def pizzaOrder():
    print("Welcome to Python Pizza Deliveries")
    print("Small Pizza: $15")
    print("Medium Pizza: $20")
    print("Large Pizza: $25")

    print(f"\nPepperoni for Small Pizza: +$2")
    print(f"Pepperoni for Medium Pizza: +$1")
    print(f"\nCheese for any Pizza: +$1")

    size = input("What size of pizza do you want?(S,M,L): ")
    add_pepperoni = input("Do you want to add pepperoni?(Y,N): ")
    extra_cheese = input("Do you want extra cheese?(Y,N): ")
    total_price = 0
    if size == 'S':
        total_price = 15
    elif size == 'M':
        total_price = 20
    elif size == 'L':
        total_price = 35

    if add_pepperoni == 'Y':
        if size == 'S':
            total_price += 2
        else:
            total_price += 3

    if extra_cheese == 'Y':
        total_price += 1

    print(f"Your final bill is ${total_price}")


def loveCalculater():
    print("Welcome to the Love Calculater")
    name1 = input("What is your name: ")
    name2 = input("What is their name: ")

    combined_name = name1 + name2
    combined_name = combined_name.lower()
    l = combined_name.count('l')
    o = combined_name.count('o')
    v = combined_name.count('v')
    e = combined_name.count('e')
    tens = (l + o + v + e)

    t = combined_name.count('t')
    r = combined_name.count('r')
    u = combined_name.count('u')
    e = combined_name.count('e')
    ones = (t + r + u + e)
    love_score = int(f"{ones}{tens}")

    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, go to together like coke and mentos")
    elif 40 <= love_score <= 50:
        print(f"Your score is {love_score}, your alright together")
    else:
        print(f"Your score is {love_score}")


# Day 3 Project

def treasureIsland():
    print('''
    *******************************************************************************
              |                   |                  |                     |
     _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
              |                `"=._o`"=._      _`"=._                     |
     _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
              |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
     _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    direction = input("You're at a crossroad, where do you want to go? Type 'left' or 'right': ").lower()
    if direction == 'left':
        wait_or_swim = input(
            "You've come to a lake. There is an Island in the middle of the lake. Type 'wait' or 'swim': ").lower()
        if wait_or_swim == 'wait':
            door = input(
                "You arrived at the Island unharmed.There is a house with 3 door One is RED, one is BLUE and One is YELLOW Which Color you choose 'Blue', 'Yellow' & 'Red':").lower()
            if door == 'yellow':
                print("You find the Treasure You Win!")
            elif door == 'red':
                print("It's ful of fire, Game Over")
            elif door == 'blue':
                print("Your enter a room of beast. Game Over")
            else:
                print("You choose wrong door, Game Over")
        else:
            print("You got attacked by an angry trout, Game Over")
    else:
        print("You fell into hole, Game Over")


if __name__ == '__main__':
    rollercoaster()
    bmiCalculater()
    leapYear()
    pizzaOrder()
    loveCalculater()
    treasureIsland()
