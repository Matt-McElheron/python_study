#!/usr/bin/python3

# Task:     Rosalind problem FIB.
# Input:    Positive integers n ≤ 40 and k ≤ 5.
# Output:   The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
#           generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs
#           (instead of only 1 pair).
# Date:     06/06/2020


# The sys module allows intake of input variables.
import sys


# This is the function which will be used to compute the answer to the task, receiving month and offspring/generation
# as input parameters
def fibonacci(n_months, k_offspring):

    # Prior to operating on any variables, me must first ensure that they are integers.
    # This try block converts the input variables from strings to integers.
    try:
        n_months = int(n_months)
        k_offspring = int(k_offspring)

    # If the input variables are not numbers as requested, an error message will be printed and the program exited.
    except ValueError:
        print("The correct input format has not been followed.\n"
              "Please provide positive integers n ≤ 40 and k ≤ 5.")
        exit()

    # Once the try checkpoint is passed, the rabbit number is generated.
    # The conventional Fibonacci sequence follows the format of "Fn = (Fn-1) + (Fn-2)"
    # For this task, each mature rabbit pair will produce k offspring pairs, instead of 1.
    # Thus, a formula of "Fn = (Fn-1) + k(Fn-2)" will be used, up to a value of n provided.

    # Here, we set month 0 and month 1 to a value of 1. This is because we assume a starting value of 1, and a
    # maturation time of 1 month (hence the formula).
    # These values will provide our initial (Fn-1) and (Fn-2).
    fminus2 = 1
    fminus1 = 1

    # This is the forumala which will be used to compute the answer for n months.
    fn = fminus1 + k_offspring * fminus2

    # To calculate, we count up to n-2. This is because we already know the initial values for month 0 and 1 (both 1).
    for i in range(1, n_months-1):

        # Each iteration/month, we update our counter
        # Fn, our current count becomes the sum of the last month's count (Fn-1) plus the offspring of our mature
        # rabbits (Fn-2 multiplied by offspring/generation multiplier, k)
        fn = fminus1 + k_offspring*fminus2

        # In addition, we update our Fn-1/Fn-2 values. Fn-1 (fminus1) becomes Fn-2 (is assigned to fminus2)
        fminus2 = fminus1

        # The current generation value (fn) will become Fn-1 in the next month, and so is assigned to fminus1.
        fminus1 = fn

    # The answer is then returned.
    return fn


# This main function is unnecessary for this rosalind problem, but is here to be consistent with the usual structure.
def main(n_months, k_offspring):
    rabbit_num = fibonacci(n_months, k_offspring)

    print(rabbit_num)


# Here we execute our code, first checking that two variables have been entered.
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])

    else:
        print("The correct input format has not been followed.\n"
              "Please provide positive integers n ≤ 40 and k ≤ 5")
