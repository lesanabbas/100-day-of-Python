from art import logo
import os
def is_leap(year):

    '''This function return true or false leep year'''

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
  if month > 12 or month < 1:
    return "Invalid"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if is_leap(year) and month == 2:
    return 29
  return 28
  return month_days[month - 1]

# Day 8 Project

def add(n1 , n2):
      return n1+n2

def subs(n1, n2):
  return n1-n2

def mult(n1, n2):
  return n1*n2

def div(n1, n2):
  try:
    return int(n1/n2)
  except:
    return "Divide by zero Exception"
  return -1

operations = {
  "+": add,
  "-": subs,
  "*": mult,
  "/": div
}

def calculator():
      print(logo)
      num1 = float(input("What's the first number?: "))

      for symbol in operations:
            print(symbol)
      should_continue = True

      while should_continue:
            symbol = input("Pick an operation: ")
            num2 = float(input("What's the next number?:  "))
            cal_function = operations[symbol]
            result = cal_function(num1, num2)
            print(f"{num1} {symbol} {num2} = {result}")

            if input(
              f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  "
            ) == 'y':
              num1 = result
            else:
                  should_continue = False
                  os.system('cls')
                  calculator()

      

if __name__ == '__main__':
    # year = int(input("Enter a year: "))
    # month = int(input("Enter a month: "))
    # days = days_in_month(year, month)
    # print(days)
    calculator()
    

          
    