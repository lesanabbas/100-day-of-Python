print(":Welcome to the Tip Calculator:")
print("-------------------------------")
amount = float(input("What was the total bill: ₹"))
tip = int(input("What percentage tip would you like to give 10, 20, 15?: "))
people_count = int(input("How many people to split bill: "))

bill_with_tip = tip / 100 * amount + amount
total = "{:.2f}".format(bill_with_tip/people_count)
print(f"Each people should pay: {total}")