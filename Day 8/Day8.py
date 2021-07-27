import math
from art import logo
def greet_with(name, location):
    print(f"Hello! {name}")
    print(f"What is it like in {location}")


def paint_calc(height, width, coverage):
    res = math.ceil((height * width) / coverage)
    print(f"You'll need {res} cans of paint")

def prime_checker(num):
    flag = 0
    for i in range(1, num+1):
        if num%i == 0:
            flag += 1
        
    if flag > 2:
        print("It's not a prime number")
    else:
        print("It's a prime number")


# def encrypt(plain_text, shift_amount):
#     cipher_text = ''
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter

#     print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
        
#     print(f"The decoded text is {plain_text}")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""

    if cipher_direction == "decode":
            shift_amount *= -1

    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"Here's the {direction} result: {end_text}")

from art import logo
print(logo)

    

if __name__ == '__main__':
    # greet_with(name="Kaif", location="Kanpur")
    # test_h = int(input("Enter height of wall: "))
    # test_w = int(input("Enter width of wall: "))
    # coverage = 5
    # paint_calc(test_h,test_w,coverage)


    should_end = False
    while not should_end:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        shift = shift % 26

        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        if restart == 'no':
            should_end = True
            print("GoodBye")


    
    