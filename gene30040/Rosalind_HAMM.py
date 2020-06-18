#!/usr/bin/python3

# Task:     Rosalind problem HAMM.
# Input:    A file containing two DNA strings, s and t.
# Output:   The Hamming distance dH(s,t).
# Date:     06/06/2020


# The sys module allows intake of input variables.
import sys


# This main function allows us to create the variables we need and inspect the input.
def main(input_file):

    # This list variable will capture any sequences from the input file.
    seq_list = []

    # This variable will count every time two nucleotides are different.
    diff_counter = 0

    # We read the input file.
    with open(input_file) as fin:

        # We then iterate over every line in the file, and add the stripped lines to our list.
        for line in fin:
            seq_list.append(line.strip())

        # We then iterate across the length of each seq..
        for i in range(0, len(seq_list[0])):

            # .. using each iterable as an index for the bases of the inputted seq, which have been stored in our list.
            # Using this index, we compare the base of each inputted seq.
            if seq_list[0][i] != seq_list[1][i]:

                # if the bases are different, we increase our counter by 1.
                diff_counter += 1

        # Once counting is completed, we can print our answer.
        print(diff_counter)


# Here we execute our code, first checking that a file has been provided.
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])

    else:
        print("The correct input format has not been followed.\n"
              "Please provide a file containing two sequences.")
