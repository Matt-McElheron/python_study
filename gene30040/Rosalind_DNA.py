#!/usr/bin/python3

# Task:     Rosalind problem "DNA".
# Input:    A DNA string s of nucleotides.
# Output:   Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G',
#           and 'T' occur in s.
# Date:     31/05/2020


# The sys module allows intake of input variables.
import sys


# This function will generate a nucleotide count using the count function.
def base_counter(s):
    return s.count("A"), s.count("C"), s.count("G"), s.count("T")


# This is the function which will be used to generate a nucleotide count using a dictionary.
def base_dicter(str_input):

    # We define a dict to capture and count each nucleotide.
    # We will use each nucleotide as a key, and the count as a value. Each count of course begins at zero.
    counter_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

    # We iterate over every base/character in the string.
    for base in str_input:

        # for each base, we ensure that it is upper case, and then add plus 1 to our counter
        try:
            base = base.upper()
            counter_dict[base] += 1

        # If the characters provided do not fulfill the requested format, an error message is printed.
        except KeyError:
            print("Error 101: the correct input format has not been followed.\n "
                  "Please provide a DNA string s of nucleotides.")
            exit()

    # We then return our dictionary. Technically speaking, returning a dict is not necessary.
    return counter_dict


# This main function calls one of our counter functions, and then print out our answer.
def main(str_input):

    # The count is generated here using the .count function.
    """
    nuc_count = base_counter(str_input)
    print(nuc_count[0], nuc_count[1], nuc_count[2], nuc_count[3])
    """

    # The count is made here using a dictionary in this function.
    nuc_dict = base_dicter(str_input)

    # The requested output is then printed to screen.
    print(nuc_dict["A"], nuc_dict["C"], nuc_dict["G"], nuc_dict["T"])

    # For improved output formatting, the following could be used:
    """
    for key, value in nuc_dict.items():
        print("{} count: {}".format(key, value))
    """

    return


# Here we execute our code, first checking that the input is correct.
if __name__ == "__main__":

    # This line checks if the string has been given as a command line argument, and then uses it.
    if len(sys.argv) == 2:
        input_string = sys.argv[1]
        main(input_string)

    # This elif block checks if no command line arguments have been given.
    # If none are given, this block will ask the user to input the string manually.
    elif len(sys.argv) == 1:
        input_string = input("Please provide a DNA string of nucleotides:\n")
        main(input_string)

    # If too many command line arguments have been given, the code will produce an error message plus an instruction.
    else:
        print("The correct input format has not been followed.\n"
              "Please provide a DNA string s of nucleotides.")
