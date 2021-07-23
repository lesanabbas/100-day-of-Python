import random as r


def coinFlip():
    random_int = r.randint(1, 2)
    if random_int == 1:
        print("Heads")
    else:
        print("Tails")


def billPay():
    print("Who will pay the bill")
    name = input("Enter name list with space: ")
    name = name.split(" ")
    print(f"{name[r.randint(0, len(name))]} is going to pay today!")


def treasureMap():
    row1 = ['⬜️', '⬜️', '⬜️']
    row2 = ['⬜️', '⬜️', '⬜️']
    row3 = ['⬜️', '⬜️', '⬜️']
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")

    number = input("Where do you want to put the treasure? ")

    col = int(number[0])
    row = int(number[1])

    map[row - 1][col - 1] = " X  "

    print(f"{row1}\n{row2}\n{row3}")


def rockPaperScissor():
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    print("What do you choose?")
    print("0 for Rock")
    print("1 for Paper")
    print("2 for Scissors")

    option = [rock, paper, scissors]
    ch_random = r.randint(0, 2)

    ch = int(input("Enter a number: "))

    if ch >= 3 or ch < 0:
        print("invalid number")
    else:
        print("User chose: ")
        print(option[ch])

        print("Computer chose: ")
        print(option[ch_random])

        if ch == 0 and ch_random == 1:
            print("You Win!")
        elif ch_random == 0 and ch == 1:
            print("You lose!")
        elif ch < ch_random:
            print("You lose!")
        elif ch_random < ch:
            print("You Win!")
        elif ch == ch_random:
            print(f"Draw")


if __name__ == '__main__':
    rockPaperScissor()
