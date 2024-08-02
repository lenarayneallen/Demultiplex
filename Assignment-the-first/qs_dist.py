#!/usr/bin/env python
import bioinfo
import matplotlib.pyplot as plt
import gzip
import argparse

def get_args():
    parser = argparse.ArgumentParser(description = "")
    parser.add_argument("-l", "--read_length", help = "read length", required=True, type=int)
    parser.add_argument("-f", "--filename", help = "name of FASTQ file", \
                        required=True, type=str)
    parser.add_argument("-r", "--read_number", required = True, type=int)
    return parser.parse_args()

args = get_args()

#come back and use argparse for these variables
f = str(args.filename)
read_length = int(str(args.read_length))
r = int(str(args.read_number))
#initalize list
def init_list(lst: list, value: float=0.0) -> list:
    i = 0
    while i < read_length:
        lst.append(value)
        i += 1
    return lst

base_pos_list = []
base_pos_list = init_list(base_pos_list)

#populate list by summing quality scores in each base position
with gzip.open(f, "rt") as fh:
    count = 0
    for line in fh:
        line = line.strip('\n')
        count += 1
        if count % 4 == 0:
            for pos, sym in enumerate(line):
                base_pos_list[pos] += bioinfo.convert_phred(sym)

#caluclate mean quality score for each position and repopulate list with those means
for i, qs_sum in enumerate(base_pos_list):
    mean_qs = qs_sum/(count/4)
    base_pos_list[i] = round(mean_qs, 6)

#plot histogram of mean quality scores at each position
pos_list = []
mean_qs_list = []

for i, mean_qs in enumerate(base_pos_list):
    pos_list.append(i)
    mean_qs_list.append(mean_qs)

plt.bar(pos_list, mean_qs_list, color = 'xkcd:yellow orange')
plt.title(f"Mean quality score of each base position across all reads: R{r}")
plt.xlabel("Base Position")
plt.ylabel("Mean quality score")
plt.savefig(f'hist_R{r}.png')
