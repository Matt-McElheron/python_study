#!/usr/bin/python3

# Task:     Rosalind problem ini5.
# Input:    A file containing at most 1000 lines.
# Output:   A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
# Date:     31/05/2020


# The sys module allows intake of input variables.
import sys


# This is the function which will be used to write the even lines to the output file.
def write_even(fin, fout):

    # This variable will be used to iterate through even lines of the input file
    linecount = 1

    # We iterate over each line of the input file
    for line in fin:

        # Having assumed 1-based counting, "linecount" represents which line we are on.
        # If the line is odd, we add 1 to our counter and move to the next line.
        if linecount % 2 == 1:
            linecount += 1
            continue

        # If the line is even, we write the line into out output file.
        # We then add 1 to our counter and move to the next line.
        else:
            fout.write(line)
            linecount += 1
    return


# This main function is unnecessary for this rosalind problem, but is here to be consistent with the usual structure.
def main(in_file, out_file):
    with open(in_file) as fin, open(out_file, "w+") as fout:
        write_even(fin, fout)

    return


# Here we execute our code, first checking that two variables have been entered.
if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1], sys.argv[2])

    else:
        print("The correct input format has not been followed.\n"
              "Please provide a text file and an output file name.")
