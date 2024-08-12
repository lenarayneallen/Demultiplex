# Demultiplexing report

## Scripts used for demultiplexing:
Demultiplexing algorithm: [demulti_pt3.py](https://github.com/lenarayneallen/Demultiplex/blob/47d2fb9b2b404d22d1b7d972b0b566176becc3eb/Assignment-the-third/demulti_pt3.py)

SBATCH script used to run `demulti_pt3.py`: [demulti_script.sh](https://github.com/lenarayneallen/Demultiplex/blob/47d2fb9b2b404d22d1b7d972b0b566176becc3eb/Assignment-the-third/demulti_script.sh)

Script used to generate plots with matplotlib: [plotting.py](https://github.com/lenarayneallen/Demultiplex/blob/47d2fb9b2b404d22d1b7d972b0b566176becc3eb/Assignment-the-third/plotting.py)

Input file for generating plots: [dual_matched.tsv](https://github.com/lenarayneallen/Demultiplex/blob/47d2fb9b2b404d22d1b7d972b0b566176becc3eb/Assignment-the-third/dual_matched.tsv)

## Lab Notebook:
[Lab_Notebook_Demultiplexing_Part3.md](https://github.com/lenarayneallen/Demultiplex/blob/47d2fb9b2b404d22d1b7d972b0b566176becc3eb/Assignment-the-third/Lab_Notebook_Demultiplexing_Part3.md)

## Quality Score Cutoff:
- The quality score for each base in an index read must be >= 30. An index read containing a quality score less than 30 will be considered "unknown". 

## Rough statistics
- **Total number of dual matched read-pairs:** 226715602
- **Total number of index-hopped read-pairs:** 330975
- **Total number of read-pairs with unknown indexes:** 136200158
- **Percent of read-pairs with index-hopping:** 0.091%

## Stats for all samples (with dual-matched indexes)

| Sample | Index | Index sequence | % read-pairs | # of read-pairs |
| --- | --- | --- | --- | --- |
| 1 | B1 | GTAGCGTA | 2.235% | 8119243 |
| 2 | A5 | CGATCGAT | 1.543% | 5604966 |
| 3 | C1 | GATCAAGG | 1.813% | 3641072 |
| 4 | B9 | AACAGCGA | 2.442% | 8872034 |
| 6 | C9 | TAGCCATG | 2.926% | 10629633 |
| 7 | C3 | CGGTAATC | 1.394% | 5064906 |
| 8 | B3 | CTCTGGAT | 9.629% | 34976387 |
| 10 | C4 | TACCGGAT | 21.023% | 76363857 |
| 11 | A11 | CTAGCTCA | 4.771% | 17332036 |
| 14 | C7 | CACTTCAC | 1.154% | 4191388 |
| 15 | B2 | GCTACTCT | 2.042% | 7416557 |
| 16 | A1 | ACGATCAG | 2.187% | 7942853 |
| 17 | B7 | TATGGCAC | 3.079% | 11184304 |
| 19 | A3 | TGTTCCGT | 4.331% | 15733007 |
| 21 | B4 | GTCCTAAG | 2.431% | 8830276 |
| 22 | A12 | TCGACAAG | 1.061% | 3853350 |
| 23 | C10 | TCTTCGAC | 11.588% | 42094112 |
| 24 | A2 | ATCATGCG | 2.777% | 10087503 |
| 27 | C2 | ATCGTGGT | 1.896% | 6887592 |
| 28 | A10 | TCGAGAGT | 3.232% | 11741547 |
| 29 | B8 | TCGGATTC | 1.269% | 4611350 |
| 31 | A7 | GATCTTGC | 1.002% | 3641072 |
| 32 | B10 | AGAGTCCA | 3.115% | 11316780 |
| 34 | A8 | AGGATAGC | 2.388% | 8673180 |



## Plots

- Top three most represented samples: sample #10, sample #23, and sample #8

![sample_counts](https://github.com/user-attachments/assets/1005750d-4221-41cd-9482-b8906b7d82dc)

![sample_percent](https://github.com/user-attachments/assets/dbdb5684-1d6c-4427-994b-32727081b7a2)

## Counts for ALL observed pairs of indexes:
- See output summary file: [index_stats.txt](https://github.com/lenarayneallen/Demultiplex/blob/47d2fb9b2b404d22d1b7d972b0b566176becc3eb/Assignment-the-third/index_stats.txt)
