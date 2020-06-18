#!/usr/bin/python3

# Task:     Rosalind problem ini2.
# Input:    Two positive integers a and b.
# Output:   The integer corresponding to the square of the hypotenuse of the right triangle whose legs have
#           lengths a and b.
# Date:     31/05/2020


# The sys module allows intake of input variables.
import sys


# This is the function which will be used to compute the answer to the task.
# This function works by simply adding the squares of each input variable.
def c_squared(a, b):

    # Prior to operating on any variables, me must first ensure that they are integers.
    # This try block converts the input variables from strings to integers.
    try:
        a = int(a)
        b = int(b)

    # If the input variables are not numbers as requested, an error message will be printed and the program exited.
    except ValueError:
        print("The correct input format has not been followed.\n"
              "Please provide two positive integers a and b, each less than 1000.")
        exit()

    # Once the try checkpoint is passed, the requested integer is computed...
    csquared = a**2 + b**2

    # ...  and returned.
    return csquared


# This main function is unnecessary for this rosalind problem, but is here to be consistent with the usual structure.
def main(a, b):
    c2 = c_squared(a, b)
    return c2


# Here we execute our code, first checking that two variables have been entered.
if __name__ == "__main__":
    if len(sys.argv) == 3:
        answer = main(sys.argv[1], sys.argv[2])
        print(answer)
    else:
        print("The correct input format has not been followed.\n"
              "Please provide two positive integers a and b, each less than 1000.")
