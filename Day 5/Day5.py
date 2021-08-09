import random as r
def average_height():
    print("Calculate Average height")
    heights = input("Enter list of heights: ").split()
    for h in range(0, len(heights)):
        heights[h] = int(heights[h])

    sum = 0
    for h in heights:
        sum += h
    
    print(f"Average height: {round(sum/len(heights))}")

def highScore():
    score = input("Enter list of score: ").split()
    for s in range(0, len(score)):
        score[s] = int(score[s])
    
    max = 0
    for i in range(0, len(score)):
        if max < score[i]:
            max = score[i]

    print(f"Max Student Score: {max}")  

def addEvenNumber():
    print("Sum of even number b/w 1 to 100")
    even_sum = 0
    for i in range(1, 101):
        if i%2 == 0:
            even_sum += i
    
    print(f"Sum: {even_sum}")

def FizzBuzz():
    for i in range(1, 101):
        # if i%3 == 0 and i%5 == 0:
        if i%15 == 0:
            print("FizzBuzz")
            continue
        elif i%3 == 0:
            print('Fizz')
            continue
        elif i%5 == 0:
            print("Buzz")
            continue
        else:
            print(i)

# Day 5 Project

def PassGen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #password = ''
    # for char in range(1, nr_letters+1):
    #     password += r.choice(letters)

    # for char in range(1, nr_symbols + 1):
    #     password += r.choice(symbols)

    # for char in range(1, nr_numbers + 1):
    #     password += r.choice(numbers)

    # print(f"Password: {password}")

    password = []
    for char in range(1, nr_letters + 1):
        password.append(r.choice(letters))
    
    for char in range(1, nr_symbols + 1):
        password.append(r.choice(symbols))

    for char in range(1, nr_numbers + 1):
        password.append(r.choice(numbers))

    r.shuffle(password)
    password_str = ''
    for char in password:
        password_str += char

    print(f"Password: {password_str}")



if __name__ == '__main__':
    PassGen()
    