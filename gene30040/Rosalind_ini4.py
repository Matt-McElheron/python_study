#!/usr/bin/python3

# Task:     Rosalind problem ini4.
# Input:    Two positive integers a and b (a<b<10000).
# Output:   The sum of all odd integers from a through b, inclusively.
# Date:     31/05/2020


# The sys module allows intake of input variables.
import sys


# This is the function which will be used to compute the answer to the task.
# This function works by simply adding the squares of each input variable.
def sum_odds(a, b):

    # We set our counter to zero
    sum_ = 0

    # Prior to using our variables, me must first ensure that they are integers.
    # This try block converts the input variables from strings to integers.
    try:
        a = int(a)
        b = int(b)

    # If the input variables are not numbers as requested, an error message will be printed and the program exited.
    except ValueError:
        print("The correct input format has not been followed.\n"
              "Please provide two positive integers a and b")
        exit()

    # Once the try checkpoint is passed, the sum is computed.
    # We iterate over every number from a to b (including b, hence the addition of 1)
    for num in range(a, b+1):

        # This operation asks if the number is not divisible by 2, thus odd
        if num % 2 == 1:

            # If odd, the number is added to our count
            sum_ += num

    # After going through the range, the sum is then returned.
    return sum_


# This main function is unnecessary for this rosalind problem, but is here to be consistent with the usual structure.
def main(a, b):
    oddsum_answer = sum_odds(a, b)
    return oddsum_answer


# Here we execute our code, first checking that two variables have been entered.
if __name__ == "__main__":
    if len(sys.argv) == 3:
        answer = main(sys.argv[1], sys.argv[2])
        print(answer)
    else:
        print("The correct input format has not been followed.\n"
              "Please provide two positive integers a and b")
