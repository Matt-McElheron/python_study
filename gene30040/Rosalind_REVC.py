#!/usr/bin/python3

# Task:     Rosalind problem "REVC".
# Input:    A DNA string s of nucleotides.
# Output:   The reverse complement of s.
# Date:     06/06/2020


# The sys module allows intake of input variables.
import sys


# This function generates the reverse compliment of DNA.
def dna_revc(s):

    # This string variable will be used to generate out output.
    revc = ""

    # We iterate over the reverse, uppercase form of the input
    for base in s[::-1].upper():

        # For each base we see, we add the compliment nucleotide to our new "revc" variable.
        if base == "A":
            revc = revc + "T"
        elif base == "T":
            revc = revc + "A"
        elif base == "G":
            revc = revc + "C"
        elif base == "C":
            revc = revc + "G"

    # We then send back our new reverse compliment string.
    return revc


# This main function calls our reverse transcribing function, then prints out the answer.
def main(str_input):

    # The count is made here using a dictionary in this function.
    revc = dna_revc(str_input)

    # The requested output is then printed to screen.
    print(revc)

    return


# Here we execute our code, first checking what the input is correct.
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
