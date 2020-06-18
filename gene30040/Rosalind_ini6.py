#!/usr/bin/python3

# Task:     Rosalind problem ini6.
# Input:    A string s of length at most 10000 letters.
# Output:   The number of occurrences of each word in s, where words are separated by spaces.
#           Words are case-sensitive, and the lines in the output can be in any order.
# Date:     31/05/2020


# The sys module allows intake of input variables.
import sys


# This is the function which will be used to generate a word count.
def generate_dict(string_input):

    # We define a dict to capture and count each word
    # We will use each unique word as a key, and the count as a value
    counter_dict = {}

    # We iterate over every word in the string
    for word in string_input:

        # If the word has already been encountered, we increase the count by 1
        if word in counter_dict:
            counter_dict[word] += 1

        # If the word has not yet been encountered, we add it to our dictionary and label the count as 1
        else:
            counter_dict[word] = 1

    # We then return our dictionary
    return counter_dict


# This main function calls our counter function, and then prints out our answer.
def main(s_input):
    dict_count = generate_dict(s_input)
    for key, value in dict_count.items():
        print("{} {}".format(key, value))
    return


# Here we execute our code, first checking that multiple words have been entered.
if __name__ == "__main__":
    if len(sys.argv) >= 2:
        input_string = sys.argv[1:]
        main(input_string)

    # This block checks if no command line arguments have been given.
    # If none are given, this block will ask the user to input the string manually.
    # The user input is then converted into a list and passed into the main function.
    else:
        input_string = input("Please provide a string s of multiple words:\n").split()
        main(input_string)
