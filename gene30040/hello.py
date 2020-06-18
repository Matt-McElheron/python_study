#!/usr/bin/python3


#print("Hello World!")
def find_cost(cost, price_change):
    reaction_cost = cost*price_change
    discount_cost = 0.60 * reaction_cost

    num_codons = int(330/10)

    thirty_samps = reaction_cost*30
    twenny_samps = discount_cost*20

    shipping = 2 + (.20*49)

    total_cost = thirty_samps + twenny_samps + shipping

    print("The cost of the first 30 is " + str(thirty_samps),
          "\nThe cost of all 50 is " + str(thirty_samps+twenny_samps),
          "\nThe total cost is " + str(total_cost))

x = find_cost(5.95, 1)
print("price increased by 15%")
y = find_cost(5.95, 1.15)


""" You want to sequence 50 variants of this sequence. 
    The cost per sequencing reaction is €5.95 for the first 30 samples with a 40% discount on subsequent samples. 
    Shipping costs are €2 for the first sample and 20₵ per subsequent
"""

# 1. Calculate the number of codons in this sequence and assign it to a variable (eg. num_codons).
# 2. What is the type of num_codons?
# 3. Ensure in your code that the type of num_codons is int when it is calculated.
# 4. What is the total cost of sequencing 30 variants?
# 5. What is the cost of sequencing all 50 variants?
# 6. Calculate the cost of 50 reactions if the cost per reaction increases by 15%.