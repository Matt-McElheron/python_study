#!/usr/bin/python3

# Task:     Rosalind problem ini3.
# Input:    A string s and four integers a, b, c and d.
# Output:   The slice of this string from indices a through b and c through d (with space in between), inclusively.
# Date:     31/05/2020


# The sys module allows intake of input variables.
import sys


# This is the function which will be used to compute the answer to the task.
# This function works by simply adding the squares of each input variable.
def slice_string(s, a, b, c, d):

    # Prior using our variables, me must first ensure that they are integers.
    # This try block converts the input variables from strings to integers.
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

    # If the input variables are not numbers as requested, an error message will be printed and the program exited.
    except ValueError:
        print("The correct input format has not been followed.\n"
              "Please provide a string followed by four integers a, b, c and d.")
        exit()

    # Once the try checkpoint is passed, the requested slice is captured.
    # Adding 1 to the final indices is necessary as slicing does not include the character at this position.
    s = s[a:b+1] + " " + s[c:d+1]

    # The sliced up string is returned.
    return s


# This main function is unnecessary for this rosalind problem, but is here to be consistent with the usual structure.
def main(s, a, b, c, d):
    slice_answer = slice_string(s, a, b, c, d)
    return slice_answer


# Here we execute our code, first checking that two variables have been entered.
if __name__ == "__main__":
    if len(sys.argv) == 6:
        answer = main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
        print(answer)
    else:
        print("The correct input format has not been followed.\n"
              "Please provide a string followed by four integers a, b, c and d.")
