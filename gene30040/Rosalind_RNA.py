#!/usr/bin/python3

# Task:     Rosalind problem "RNA".
# Input:    A DNA string s of nucleotides.
# Output:   The transcript of s, where each T nucleotide is replaced with a uracil nucleotide.
# Date:     06/06/2020


# The sys module allows intake of input variables.
import sys


# This function replaces T nucleotides with U nucleotides.
def dna_to_rna(s):
    return s.upper().replace("T", "U")


# This main function calls our transcribing function, and then print out our answer.
def main(str_input):

    # This function will replace any Ts with Us.
    rna_transcript = dna_to_rna(str_input)

    # The requested output is then printed to screen.
    print(rna_transcript)

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
