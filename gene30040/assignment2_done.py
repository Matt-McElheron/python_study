#!/usr/bin/env python3
# 16425804

import sys
import math


def Create_Codon_Dictionaries(codon_file, dict_for_table, dict_codon_counter1, dict_codon_total1, dict_proportion2):
    for line in codon_file:
        if 'Codon' in line:
            continue
        else:
            list_of_words = line.split()
            dict_for_table[(list_of_words[0])] = (list_of_words[-1])
            dict_codon_counter1[(list_of_words[0])] = 0
            dict_codon_total1[(list_of_words[-1])] = 0
            dict_proportion2[(list_of_words[0])] = 0
    #   Here we take the codon file line by line, first skipping the header line.
    #   As the input for these assignments is rigid, we can skip the header based on the presence of something we know is there.
    #   We split each line into a list for convenience, adding the necessary element to each dictionary.
    #   These dicts will be explained when used.
    #   [0] captures codon, [-1] captures AA, 0 sets counter to 0.


def Extract_gff_data_into_dicts(gff_in, dict_start1, dict_end1, dict_strand1, dict_haemo1, dict_length1):
    for line in gff_in:
        if "gene_name" in line:
            continue
        else:
            list_of_phrases = line.split('\t')
            dict_strand1[(list_of_phrases[8])] = (list_of_phrases[5])
            dict_haemo1[(list_of_phrases[8])] = 'None'
            dict_length1[(list_of_phrases[8])] = (int(list_of_phrases[4]) + 1) - int(list_of_phrases[3])
            dict_start1[(list_of_phrases[8])] = (int(list_of_phrases[3]) - 1)
            dict_end1[(list_of_phrases[8])] = (list_of_phrases[4])
    #   Same method as during previous function.
    #   We've to account for zero-based counting.
    #   We capture start, end, length, strand and gene name.

def Capture_and_upper_sequence(fasta_in, sequence_data1):
    for line in fasta_in:
        if '>' in line:
            continue
        else:
            sequence_data1 = sequence_data1 + line.strip('\n')
    sequpper = sequence_data1.upper()
    return sequpper
    #   Here we take the fasta file, skip the header, and return sequence as a continuous, upper case string.
    #   This string can then be used later on.

def find_haemo_record_where(gff_input, dict_in):
    Q1_answer = "None"
    for line in gff_input:
        if "hemagglutination" in line:
            list_of_phrases = line.split()
            dict_in[(list_of_phrases[8])] = 'haemagglutinin present'
            Q1_answer = 'There is a haemagglutinin encoded for within the inputted sequence'
    return Q1_answer
    #   This function takes the file and determines if hemagglutination is in the description.
    #   It returns a qualitative answer to if it is encoded for within the whole sequence.
    #   It also records within a dictionary specifically which gene encodes for haemagglutinin.


def reverse_compliment_of(sequence):
    comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    sequence = [comp[key] for key in sequence]
    sequence = (''.join(sequence))[::-1]
    return sequence
    #   This function returns the reverse compliment of the string provided.


#def Question_3_component(dicstart, dicend, dict_sequence1, sequence_data2):
#    for key, value in dicstart.items():
#        dict_sequence1[key] = sequence_data2[int(dicstart[key]):int(dicend[key])]
    #   See explanation in main


def Question_3(dict_strand, dict_codon_table, dictstart, dictend, dict_sequence1, sequence_data2, dict_sequence_translation1, dict_codon_count):
    for key, value in dict_strand.items():
        dict_sequence1[key] = sequence_data2[int(dictstart[key]):int(dictend[key])]
        if value == '+':
            dict_sequence_translation1[key] = ''.join([dict_codon_table[key] for key in [(dict_sequence1[key])[i:i+3] for i in range(0, len(dict_sequence1[key]), 3)]])
            for codon in [(dict_sequence1[key])[i:i+3] for i in range(0, len(dict_sequence1[key]), 3)]:
                dict_codon_count[codon] += 1
        else:
            dict_sequence1[key] = reverse_compliment_of(dict_sequence1[key])
            dict_sequence_translation1[key] = ''.join([dict_codon_table[key] for key in [(dict_sequence1[key])[i:i+3] for i in range(0, len(dict_sequence1[key]), 3)]])
            for codon in [(dict_sequence1[key])[i:i+3] for i in range(0, len(dict_sequence1[key]), 3)]:
                dict_codon_count[codon] += 1
    #   This function does a lot in one go.
    #   The function runs through the gene_name keys of the plus/negative strand dictionary.
    #   It then assigns into a separate dictionary the splice of sequence each gene (key) is within.
    #   It does this by using the same key in both the stop- and start-point dictionaries as coordinates.
    #   Then it does an extra if the key is on the - strand (value of original dict).
    #   If negative, it first passes the sequence slice through the mandatory reverse compliment function.
    #   The function then uses a list comprehension to split the string into codons.
    #   This list comp is within a second list comp which translates the codons into AAs as part of a new list
    #   The function then assigns as a value in a new dictionary, the contents of the AA list as one continuous string.
    #   The function also includes a counter, counting the total codon usage, needed for the frequency table.



def Count_total_AA(dict_codon_counter, dict_codon_table, dict_codon_total):
    for key, value in dict_codon_counter.items():
        dict_codon_total[(dict_codon_table[key])] += value
    #   This function counts how many times each AA occurs.



def Assign_total_AA_to_codon(dict_codon_counter, dict_codon_table, dict_codon_total2, dict_proportion2):
    for key, value in dict_codon_counter.items():
        dict_proportion2[key] += dict_codon_total2[(dict_codon_table[key])]
    #   This function is key in calculating the proportion of a triplet out of the total number of its corresponding AA.
    #   Allows connecting of dictionaries when calculating proportion with the use of one 'key'.
    #   Aligning dictionaries like dominoes.


def main(gff_in, fasta_in, codon_in, output_file):


    dict_haemo = {}
    dict_start = {}
    dict_end = {}
    dict_length = {}
    dict_strand = {}
    dict_codon_table = {}
    dict_sequence = {}
    sequence_data = ''
    dict_sequence_translation = {}
    dict_codon_counter = {}
    dict_codon_total = {}
    dict_proportion = {}
#   This bit here creates all the dictionaries and the string we're going to need.
#   This can also be performed within each function, but it was mentioned that either is acceptable for the assignment.


    with open(gff_in) as gffin, open(fasta_in) as fastin, open(codon_in) as tablin, open(output_file, "w+") as fout:

        Create_Codon_Dictionaries(tablin, dict_codon_table, dict_codon_counter, dict_codon_total, dict_proportion)
        Extract_gff_data_into_dicts(gffin, dict_start, dict_end, dict_strand, dict_haemo, dict_length)
        sequence_string = Capture_and_upper_sequence(fastin, sequence_data)
    #   These functions capture the pre-requisite data/structures for handling the task.
    #   These include the sequence code, AA code and information on each gene.

        Question_1_output = find_haemo_record_where((open(gff_in)), dict_haemo)
        fout.write("##Q1\n" + Question_1_output)
        for key, value in dict_haemo.items():
            if value == 'haemagglutinin present':
                fout.write('\n' + key)
    #   The function used searches for haemo in each gene of the gff file.
    #   It returns a qualitative answer and also records within a dict which gene has haemo.
    #   The if loop then prints in the output any genes which do.

        fout.write('\n\n##Q2\n' + str(len(dict_haemo)))
    #   Question 2 does not require a standalone function.
    #   The dictionaries have recorded an entry/gene, and hence answer this question.


        #Question_3_component(dict_start, dict_end, dict_sequence, sequence_string)
    #   Here, I could have split the next function up, however that would involve more loops.
    #   The function "Question_3()" can preparing the sequence to be translated along the way.


        Question_3(dict_strand, dict_codon_table, dict_start, dict_end, dict_sequence, sequence_string, dict_sequence_translation, dict_codon_counter)
        fout.write('\n\n##Q3\n')
        for key, value in dict_sequence_translation.items():
            fout.write(key + ': ' + str(dict_length[key]) + ' nt\n' + value + '\n')
    #   Here question 3 is called.
    #   We call the key of the sequence translation dictionary to print the gene name.
    #   We use that key as the key of a separate dictionary to call the length.
    #   We then call the value of the original dictionary to print the Sequence translation.

        Count_total_AA(dict_codon_counter, dict_codon_table, dict_codon_total)
        Assign_total_AA_to_codon(dict_codon_counter, dict_codon_table, dict_codon_total, dict_proportion)
    #   Here we perform what is explained within the functions.

        fout.write('\nCodon Usage Table:\n')
        for key, value in dict_codon_counter.items():
            if value > 0:
                fout.write(key + '          ' + str(value) + '          ' + str(round(value/(dict_proportion[key]), 2)) + '\n')
            else:
                continue
    #   We first ignore the codons which aren't used.
    #   The key and the value of dict_codon_counter s simple enough as we have counted how many times each codon appears.
    #   In order to find the proportion of each codon of the total number of the corresponding AA, i.e. TTT/(all F's)..
    #   ..we needed a dictionary which links codon to total AA.
    #   It would not be possible to use the key of "TTT" to call the number of all TTT and TTC codons to count all F AAs.
    #   Hence why the dict_proportion is so helpful.

if __name__ == "__main__":
    if len(sys.argv) == 5:
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print('The correct input format has not been followed.\nPlease, in the following order, provide:\n.gff file\n.fasta file\ncodon table\noutput file')


#1:gff 2:fasta 3:codon 4:output
