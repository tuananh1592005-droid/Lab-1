import os
import time


# Colors
RESET = "\033[0m"
GREEN = "\033[48;5;22m"
RED = "\033[41m"
WHITE = "\033[47m"


# Clear console
def clear_screen():

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# =========================================
# TASK 1: FLAG OF BANGLADESH
# =========================================

def flag():

    print("TASK 1 - FLAG\n")

    for y in range(10):

        for x in range(30):

            # Red circle
            if (x - 14) ** 2 + (y - 5) ** 2 <= 16:
                print(RED + "  ", end="")

            # Green background
            else:
                print(GREEN + "  ", end="")

        print(RESET)


# =========================================
# TASK 2: PATTERN
# =========================================

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

    # Print the pattern several times
    for row in p:

        for repeat in range(3):

            for x in row:

                if x == "#":
                    print(WHITE + "  ", end="")

                else:
                    print(RESET + "  ", end="")

        print(RESET)


# =========================================
# EXTRA TASK: GRAPH y = 2x + 3
# =========================================

def graph():

    width = 9
    max_y = 19

    # Escape sequences:
    # \033[2J = clear screen
    # \033[H  = move cursor to top-left
    graph_text = "\033[2J\033[H"

    graph_text = graph_text + "EXTRA TASK - GRAPH y = 2x + 3\n\n"

    graph_text = graph_text + "y\n"
    graph_text = graph_text + "^\n"

    # Generate the whole graph
    for y in range(max_y, -1, -1):

        graph_text = graph_text + "|"

        for x in range(width):

            value = 2 * x + 3

            if y == value:
                graph_text = graph_text + " *"

            else:
                graph_text = graph_text + "  "

        graph_text = graph_text + "\n"

    # X axis
    graph_text = graph_text + "+" + "--" * width + "> x\n"

    # Print the entire graph only once
    print(graph_text, end="")


# =========================================
# TASK 3: ANIMATION
# =========================================

def animation():

    # 4 frames
    for x in [2, 7, 12, 17]:

        clear_screen()

        # Move cursor to top-left
        print("\033[H", end="")

        print("TASK 3 - ANIMATION\n")

        print(" " * x + "●")

        time.sleep(0.5)


# =========================================
# TASK 4: DIAGRAM
# =========================================

def diagram():

    print("TASK 4 - DIAGRAM\n")

    numbers = []

    # Find the folder where main.py is located
    folder = os.path.dirname(os.path.abspath(__file__))

    # sequence.txt should be in the same folder
    file_path = os.path.join(folder, "sequence.txt")

    # Read numbers from file
    with open(file_path, "r") as file:

        data = file.read().split()

    # Convert text to float numbers
    for x in data:

        numbers.append(float(x))

    # Check that file contains at least 250 numbers
    if len(numbers) < 250:

        print("Error: sequence.txt must contain at least 250 numbers.")
        return

    # Sum of absolute values of first 125 numbers
    first = 0

    for i in range(125):

        first = first + abs(numbers[i])

    # Sum of absolute values of second 125 numbers
    second = 0

    for i in range(125, 250):

        second = second + abs(numbers[i])

    # Total
    total = first + second

    if total == 0:

        print("Error: total is 0.")
        return

    # Percentages
    p1 = first / total * 100
    p2 = second / total * 100

    # Results
    print("First 125 :", round(p1, 1), "%")
    print("Second 125:", round(p2, 1), "%")

    print()

    # Diagram
    print("A:", "#" * int(p1 / 2))
    print("B:", "#" * int(p2 / 2))


# =========================================
# MAIN
# =========================================

flag()

input("\nPress Enter...")
clear_screen()


pattern()

input("\nPress Enter...")
clear_screen()


graph()

input("\nPress Enter...")
clear_screen()


animation()

input("\nPress Enter...")
clear_screen()


diagram()
