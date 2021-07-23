def tipCalculator():
    print("Welcome to the tip calculator!")
    bill_amount = float(input("What was the total bill amount: $"))
    tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
    people = int(input("How many people to split the bill?"))

    tip_amount = (bill_amount * tip) / 100
    bill_amount += tip_amount
    print(f"Each person should pay: {round(bill_amount / people, 2)}")


if __name__ == '__main__':
    tipCalculator()
