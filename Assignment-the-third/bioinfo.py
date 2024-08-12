#!/usr/bin/env python

# Author: Lena Allen lenara@uoregon.edu

# Check out some Python module resources:
#   - https://docs.python.org/3/tutorial/modules.html
#   - https://python101.pythonlibrary.org/chapter36_creating_modules_and_packages.html
#   - and many more: https://www.google.com/search?q=how+to+write+a+python+module

'''This module is a collection of useful bioinformatics functions
written during the Bioinformatics and Genomics Program coursework.
You should update this docstring to reflect what you would like it to say'''

__version__ = "0.4"         # Read way more about versioning here:
                            # https://en.wikipedia.org/wiki/Software_versioning

DNA_bases = ["A","C","G","T","N","a","c","g","t","n"]
RNA_bases = ["A","C","G","U","N","a","c","g","u","n"]

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    return ord(letter) - 33

def qual_score(phred_score: str) -> float:
    '''Given string of Phred quality scores, calculates the average quality score of that string.'''
    score_sum = 0
    for letter in phred_score:
        score_sum += convert_phred(letter)
    average_qs = score_sum/len(phred_score)
    return average_qs

def validate_base_seq(seq: str,RNAflag: bool=False) -> bool:    #use type annotation
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case insensitive.'''
    seq = seq.upper()
    return len(seq) == seq.count("A") + seq.count("U" if RNAflag else "T") + seq.count("G") + seq.count("C")


def gc_content(seq: str) -> float | None:
    '''Returns GC content of a DNA or RNA sequence as a decimal between 0 and 1.'''
    assert validate_base_seq(seq), "Seq is not DNA or RNA sequence"
    seq = seq.upper()
    return ((seq.count("G") + seq.count("C")) / len(seq))

def calc_median(lst: list) -> float | int:
    #if even
    if len(lst) % 2 == 0:
        even_index_1 = int((len(lst)/2)) - 1 
        even_index_2 = int(((len(lst))/2) + 1) - 1
        return (((lst[even_index_1]) + (lst[even_index_2])) /2 ) 
    #if odd
    else:
        median_index = int(((len(lst) + 1) / 2) - 1)
        return lst[median_index]

def oneline_fasta(file):
    '''If a fasta file contains records where sequences span multiple lines, reformat so that each sequence is contained in one line'''
    output_path = f"{file[0:5]}_output.fa"
    first = True
    with open(file, "r") as fh, open(output_path, "w") as fo:
        for line in fh:
            #if line is a header
            if line[0] == ">":
                #if it is the first line
                if first:
                    #write the header to output file
                    fo.write(line)
                    first = False
                #if header is not the first line
                else:
                    #write to output file with preceeding newline character
                    fo.write("\n" + line)
            #if line is not a header
            else:
                #strip newline
                line = line.strip('\n')
                #write the line to output file
                fo.write(line)
    return fo

if __name__ == "__main__":
    # write tests for functions above, Leslie has already populated some tests for convert_phred
    # These tests are run when you execute this file directly (instead of importing it)
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")

    #qual score
    assert qual_score("EEE") == 36
    assert qual_score("#I") == 21
    assert qual_score("EJ") == 38.5
    print("You calcluated the correct average phred score")


    #GC content
    assert gc_content("GCGCGC") == 1
    assert gc_content("AATTATA") == 0
    assert gc_content("GCATCGAT") == 0.5
    print("GC content is correct!")

    #validate base seq
    assert validate_base_seq("AATAGAT", False) == True, "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
    assert validate_base_seq("TATUC",False) == False
    assert validate_base_seq("UCUGCU", False) == False
    print("Passed DNA and RNA tests")

    #calc median
    assert calc_median([3,5,9]) == 5
    assert calc_median([10,20,35,40]) == 27.5 
    assert calc_median([4,10,33]) == 10
    print("You correctly calculated medians")