### Binary Search Algorithm ###
# - abe #####################
#########

import sys, math

min    = int(raw_input("Arbitrary Min: "))
max    = int(raw_input("Arbitrary Max: "))
total  = int(math.log(min + (max + 1), 2))
max    = max + 2
array  = range(min,max)
n      = len(array)
min    = 0
max    = n - 1
answer = str("")

print(str(total) + " max guesses needed.")

# WHILE GUESS LOOP #
while answer != "y":
        guess  = str((min + max) / 2)
        answer = raw_input("Is your number " + guess + "? (y/n) ")
        if answer == "n":
                answer = raw_input("Is your number bigger or smaller than " + guess + "? (b/s) ")
                if answer == "b":
                        min = int(guess) + 1
                elif answer == "s":
                        max = int(guess) - 1
        else:
                print("Nailed it!")
                print("")
                sys.exit
# END #
