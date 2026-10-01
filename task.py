import os
import time

RESET = "\033[0m"
GREEN = "\033[48;5;22m"
RED = "\033[41m"
WHITE = "\033[47m"


# Task 1: Flag
def flag():
    print("TASK 1 - FLAG\n")

    for y in range(10):
        for x in range(30):

            if (x - 14) ** 2 + (y - 5) ** 2 <= 16:
                print(RED + "  ", end="")
            else:
                print(GREEN + "  ", end="")

        print(RESET)


# Task 2: Pattern
def pattern():
    print("TASK 2 - PATTERN\n")

    p = [
        "###########",
        "##     ####",
        "## ### ####",
        "## #   ####",
        "## # ######",
        "## #     ##",
        "###########"
    ]

    for row in p:
        for x in row:

            if x == "#":
                print(WHITE + "  ", end="")
            else:
                print(RESET + "  ", end="")

        print(RESET)


# Extra task: y = 2x + 3
def graph():
    print("GRAPH y = 2x + 3\n")

    for x in range(9, 0, -1):
        y = 2 * x + 3
        print(" " * y + "*")


# Task 3: Animation
def animation():

    for x in [2, 7, 12, 17]:

        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

        print("TASK 3 - ANIMATION\n")

        print(" " * x + "●")

        time.sleep(0.5)


# Task 4: sequence.txt
def diagram():

    print("TASK 4 - DIAGRAM\n")

    numbers = []

    with open("sequence.txt", "r") as file:
        data = file.read().split()

    for x in data:
        numbers.append(float(x))

    first = 0

    for i in range(125):
        first = first + abs(numbers[i])

    second = 0

    for i in range(125, 250):
        second = second + abs(numbers[i])

    total = first + second

    p1 = first / total * 100
    p2 = second / total * 100

    print("First 125 :", round(p1, 1), "%")
    print("Second 125:", round(p2, 1), "%")

    print("A:", "#" * int(p1 / 2))
    print("B:", "#" * int(p2 / 2))


# MAIN

flag()

input("\nEnter...")

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


pattern()

input("\nEnter...")

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


graph()

input("\nEnter...")

animation()


if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")


diagram()
