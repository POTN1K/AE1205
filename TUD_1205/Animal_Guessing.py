# Assignment Two. A program capable of guessing your animal
# Author: Nikolaus Ricker

# ------------------------------------------------------
# Functions
def yes_no(ans_):
    if ans_ == ('n' or 'N' or 'no' or 'No' or 'NO'):
        return False
    if ans_ == ('y' or 'Y' or 'yes' or 'Yes' or 'YES'):
        return True
    else:
        print("Give a valid answer")
        yes_no(input())


# -----------------------------------------------------
# Gaming loop
game = True
while game:
    # ---------------------------------------------------
    # Libraries
    import os

    # Constants

    # Variables
    table = []
    n = 1
    loop = True
    supertable = []

    # ---------------------------------------------
    # Read data from table
    dat_file = r"Data/Animal Guessing/animals.dat"

    with open(dat_file) as dat:
        for line in dat.readlines():
            table.append(line.strip("\n").split(" -- "))

    for i in table:
        temp = []
        for ind, item in enumerate(i):
            if item.isdigit():
                j = int(item)
                temp.append(j)
            else:
                temp.append(item)
        supertable.append(temp)
    table = supertable
    # -----------------------------------------------
    # Ask question
    print("Think of an animal, I'll try to guess it")
    while loop:
        print(table[n - 1][1])
        answ = yes_no(input())
        if answ:
            x = table[n - 1][2]
        else:
            x = table[n - 1][3]

        if type(x) == int:
            n = x + 1
        else:
            loop = False

    print("I think I know it!!")
    print(f"Is it a {x}?")
    ans = yes_no(input())

    if ans:
        print("Yeah, I did it")
    else:
        print("That's a shame")
        # --------------------------------------------------
        # Learning algorithm
        print("What is the right answer?")
        animal = input()
        print(f"Give me a yes/no question to distinguish between {animal} and {x}")
        question = input()
        print(f"What is the answer for {animal}?")
        ans = yes_no(input())
        n_quest = len(table)

        if ans:
            guess = [n_quest, question, animal, x]
        else:
            guess = [n_quest, question, x, animal]

        table.append(guess)
        if answ:
            table[n - 1][2] = n_quest
        else:
            table[n - 1][3] = n_quest

        print(table)
        # -----------------------------------------------------
        # Rewrite file

        with open(dat_file, "w") as dat:
            for l, j in enumerate(table):
                txt = f"{table[l][0]} -- {table[l][1]} -- {table[l][2]} -- {table[l][3]}\n"
                dat.write(txt)
    # --------------------
    print("Wanna play again?")
    game = yes_no(input())
