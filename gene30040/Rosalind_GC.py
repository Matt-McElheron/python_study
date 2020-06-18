#!/usr/bin/python3

# Task:     Rosalind problem GC.
# Input:    A file of DNA strings in FASTA format.
# Output:   The ID of the string having the highest GC-content, followed by the GC-content of that string.
# Date:     06/06/2020


# The sys module allows intake of input variables.
import sys


# This is the function which will be used to calculate GC content.
def gc_counter(seq):

    # We first find out how many G and C occur in the sequence.
    gc_count = seq.count("G") + seq.count("C")

    # We then return this value as a percentage of the total bases
    return (gc_count/len(seq))*100


# This main function allows us to create any variables we need, and call the relevant functions.
def main(input_file):

    # This dictionary is going to let us store all GC data (value) with the corresponding, unique FASTA header (key).
    # The "biggest_id" key will help us keep track of the highest GC content.
    gc_dict = {"biggest_gc": 0}

    # We read the input file.
    with open(input_file) as fin:

        # We then iterate over every line in the file.
        for line in fin:

            # If the line is a header (i.e. ">..."), we will operate on this line and the sequence string which follows.
            if ">" in line:

                # We take the sequence string data in the following line, and pass it through a gc_counter function.
                # What pops out of this gc_counter function, is then assigned as a value into the GC dictionary, with
                # the corresponding fasta header as the key.
                gc_dict[line.strip()] = gc_counter(next(fin).strip())

                # If the current GC content being examined is the biggest recorded so far, it will be stored in the
                # dictionary alongside the "biggest_gc" key.
                if gc_dict[line.strip()] > gc_dict["biggest_gc"]:
                    gc_dict["biggest_gc"] = gc_dict[line.strip()]

                    # We also set a second variable to be the header ID for the value
                    biggest_id = line.strip()

    # We can then use the ID's stored as the biggest to print our final answer.
    print(biggest_id.strip(">"), str(round(gc_dict["biggest_gc"], 6)) + "%")


# Here we execute our code, first checking that a file has been provided.
if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])

    else:
        print("The correct input format has not been followed.\n"
              "Please provide a FASTA file.")
