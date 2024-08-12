#!/usr/bin/env python

from itertools import product
import bioinfo
import gzip
import argparse

def Fail_QS_Thresh(qualscore_string: str, cutoff: int) -> bool:
    '''If a single base quality score in qualscore_string is below the provided cutoff, return True. Otherwise, return False.'''
    for sym in qualscore_string:
        if bioinfo.convert_phred(sym) < cutoff:
            return True
    return False

def ReverseComplement(seq: str) -> str:
    '''Returns the reverse complement of a sequence'''
    complement_dict = {"A":"T", "T":"A", "C":"G", "G":"C", "N":"N"}
    seq_list = list(seq)
    seq_list.reverse()
    comp_list = [complement_dict[base] for base in seq_list]
    rev_comp = "".join(comp_list)
    return rev_comp

def AppendIndexes(header: str, index1: str, index2: str) -> str:
    '''Appends index1 and index2 to the provided header in the following format: header index1-index2'''
    new_header = f"{header} {index1}-{index2}"
    return new_header

#using argparse to define variables from the command line
def get_args():
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("-r1", "--R1_fastq", required=True, type=str)
    parser.add_argument("-r2", "--R2_fastq", required=True, type=str)
    parser.add_argument("-r3", "--R3_fastq", required=True, type=str)
    parser.add_argument("-r4", "--R4_fastq", required=True, type=str)
    parser.add_argument("-i", "--indexes", required=True, type=str)
    parser.add_argument("-qst", "--qs_thresh", required=True, type=int)
    return parser.parse_args()

args = get_args()

indexes = str(args.indexes)
bio_R1 = str(args.R1_fastq)
ind_R2 = str(args.R2_fastq)
ind_R3 = str(args.R3_fastq)
bio_R4 = str(args.R4_fastq)
qst = int(args.qs_thresh)

#make list of index sequences
with open(indexes, "r") as fi:
    sample_num_list = []
    index_list = []
    for i,line in enumerate(fi):
        if i != 0:
            line = line.strip("\n")
            line = line.split("\t")
            index_list.append(line[4])
            sample_num_list.append(line[0])

#index_permutations
#each pair of indexes is a tuple
index_perms = list(product(index_list,repeat=2))

#create dictionary for index pairs, where key = index and value = a counter
index_pair_dict = {i:0 for i in index_perms}

#create dictionary where keys = indexes and values = the associated R1 and R2 filehandles
ind_filename_dict = {}

#open R1 and R2 files for all valid indexes 
for index in index_list:
    ind_filename_dict[index] = [open(f"{index}_R1.fastq", "w"), open(f"{index}_R2.fastq", "w")] 

#initialize counters for matched, hopped, and unknown indexes
matched = 0
hopped = 0   
unknown = 0

#open all files for reading (biological and index fastq files) and writing (output files for hopped and unknown reads)
with gzip.open(bio_R1, "rt") as R1, gzip.open(bio_R4, "rt") as R4, gzip.open(ind_R2, "rt") as R2, gzip.open(ind_R3, "rt") as R3, open("unknown_R1.fastq", "w") as u1, open("unknown_R2.fastq", "w") as u2, open("hopped_R1.fastq", "w") as h1, open("hopped_R2.fastq", "w") as h2:
        #initialize empty lists to hold current records for each file
        R1_record = []
        R2_record = []
        R3_record = []
        R4_record = []

        #iterate through all files simultaneously to append current record
        for R1_line, R2_line, R3_line, R4_line in zip(R1, R2, R3, R4):
            R1_line = R1_line.strip()
            R2_line = R2_line.strip()
            R3_line = R3_line.strip()
            R4_line = R4_line.strip()
            
            R2_record.append(R2_line)
            R3_record.append(R3_line)
            R1_record.append(R1_line)
            R4_record.append(R4_line)

            #if a full record has been added to each list
            if len(R2_record) == 4:
                #extract the indexes, taking the reverse complement of R3
                index2 = R2_record[1]
                index3 = ReverseComplement(R3_record[1])
                #append indexes to the headers for R1 and R4
                R1_header = AppendIndexes(R1_record[0],index2, index3)
                R4_header = AppendIndexes(R4_record[0],index2, index3)

                #are the indexes valid? if not, write to unknown
                if (index2 not in index_list) or (index3 not in index_list) or (Fail_QS_Thresh(R2_record[3], 30) == True ) or (Fail_QS_Thresh(R3_record[3], 30) == True):
                    u1.write(f"{R1_header}\n")
                    for i, line in enumerate(R1_record):
                        if i != 0:
                            u1.write(f"{line}\n")
                    u2.write(f"{R4_header}\n")
                    for i, line in enumerate(R4_record):
                        if i != 0:
                            u2.write(f"{line}\n")
                    #increment unknown counter
                    if (index2,index3) not in index_pair_dict.keys():
                        index_pair_dict[(index2, index3)] = 1
                        unknown += 1
                    else:
                        index_pair_dict[(index2, index3)] += 1
                        unknown += 1

            
                #do the indexes match? if so, write to file containing index name 
                elif index2 == index3:
                    ind_filename_dict[index2][0].write(f"{R1_header}\n")
                    for i, line in enumerate(R1_record):
                        if i != 0:
                            ind_filename_dict[index2][0].write(f"{line}\n")

                    ind_filename_dict[index2][1].write(f"{R4_header}\n")
                    for i, line in enumerate(R4_record):
                        if i != 0:
                            ind_filename_dict[index2][1].write(f"{line}\n")
                    
                    #increment counter
                    index_pair_dict[(index2, index3)] += 1
                    matched += 1

                #are the indexes valid but unmatched? if so, write to hopped
                else: 
                    h1.write(f"{R1_header}\n")
                    for i, line in enumerate(R1_record):
                        if i != 0:
                            h1.write(f"{line}\n")
                    h2.write(f"{R4_header}\n")
                    for i, line in enumerate(R4_record):
                        if i != 0:
                            h2.write(f"{line}\n")

                    #increment counter
                    if (index2,index3) not in index_pair_dict.keys():
                        index_pair_dict[(index2, index3)] = 1
                        hopped += 1
                    else:
                        index_pair_dict[(index2, index3)] += 1
                        hopped += 1
                #clear record lists
                R1_record = []
                R2_record = []
                R3_record = []
                R4_record = []

#generate summary report

#calculate percent of indexes that are hopped
percent_hopped = (hopped/sum(index_pair_dict.values())) * 100

#open file to write index stats to
with open("index_stats.txt", "w") as isf:
    isf.write(f"Dual Matched Total:\t{matched}\n")
    isf.write(f"Index Hopped Total:\t{hopped}\n")
    isf.write(f"Percent of Index Swapping:\t{percent_hopped}%\n")
    isf.write(f"Unknown Index Total:\t{unknown}\n\n\n")
    isf.write("Percentage of reads from each sample:\n")
    #calculate percent reads from each sample
    for i,index in enumerate(index_list):
        for indexpair in index_pair_dict:
            if index == indexpair[0] == indexpair[1]:
                perc_sample = (index_pair_dict[indexpair]/sum(index_pair_dict.values()) * 100)
                isf.write(f"Sample {sample_num_list[i]}\t{perc_sample}%\n")
    isf.write(f"\n\nNumber of reads for each index pair:\n")
    #write counts for each index pair observed
    for indexpair in index_pair_dict:
        isf.write(f"{indexpair[0]}-{indexpair[1]}:\t{index_pair_dict[indexpair]}\n")
       