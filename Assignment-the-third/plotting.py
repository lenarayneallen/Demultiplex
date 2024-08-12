import matplotlib.pyplot as plt
with open("dual_matched.tsv", "r") as dm:
    samples = []
    ind_seqs = []
    counts = []
    percent_reads = []
    for line in dm:
        line = line.strip("\n")
        line = line.split("\t")
        samples.append(line[0])
        ind_seqs.append(line[1])
        counts.append(int(line[2]))
        percent_reads.append(float(line[3]))

print(samples)
print(percent_reads)

#percentage 
plt.bar(samples, percent_reads, color = 'xkcd:yellow orange')
plt.title("Demultiplexing: Percentage of Total Read-Pairs From Each Sample")
plt.xlabel("sample")
plt.ylabel("percent of all reads")
plt.xticks(rotation=45)
plt.savefig("sample_percent.png")

#counts
plt.bar(samples, counts, color = 'xkcd:reddish purple')
plt.title("Demultiplexing: Number of Read-Pairs per Sample")
plt.xlabel("sample")
plt.ylabel("Number of Read Pairs")
plt.xticks(rotation=45)
plt.savefig("sample_counts.png")
