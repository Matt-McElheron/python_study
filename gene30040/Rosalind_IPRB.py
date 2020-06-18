#!/usr/bin/python3

# Task:     Rosalind problem IPRB.
# Input:    Three positive integers k, m, and n, representing a population containing k+m+n organisms:
#           k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Output:   The probability that two randomly selected mating organisms will produce an individual possessing
#           a dominant allele, assuming all organisms can mate.
# Date:     31/05/2020


# The sys module allows intake of input variables.
import sys


# This main function is unnecessary for this rosalind problem, but is here to be consistent with the usual structure.
def main(kmn_list):

    # This variable will become out population size
    popsize = 0

    # This variable will be used to sum our odds of a dominant phenotype.
    odds = 1

    # We iterate over our list of inputted values k, m, and n.
    for i in range(0, len(kmn_list)):

        # We make sure our values are integers.
        kmn_list[i] = int(kmn_list[i])

        # We then add the value to our total value
        popsize += kmn_list[i]

    # The odds of getting a dominant genotype (AA or Aa) are the odds of not getting a recessive genotype (aa)

    # this means we can subtract the odds of two n individuals mating...
    odds -= ((kmn_list[2]/popsize) * ((kmn_list[2]-1)/(popsize-1)))

    # .. and subtract the odds of an n individual receiving a dominant allele from an m individual.
    odds -= (kmn_list[2] / popsize) * (kmn_list[1] / (popsize - 1)) * 0.50

    # .. and subtract the odds of an m individual passing on its recessive allele with an n individual.
    odds -= ((kmn_list[1]/popsize) * .50 * (kmn_list[2]/(popsize-1)))

    # .. and subtract the odds of to m individuals passing on their recessive alleles.
    odds -= ((kmn_list[1]/popsize) * ((kmn_list[1] - 1) / (popsize - 1))) * (0.5 ** 2)

    print(round(odds, 5))



    #probab = mating_chance(k, m, n)
    #return probab


# Here we execute our code, first checking that three variables have been entered.
if __name__ == "__main__":
    if len(sys.argv) == 4:
        answer = main(sys.argv[1:])
        print(answer)
    else:
        print("The correct input format has not been followed.\n"
              "Please provide Three positive integers k, m, and n.")
