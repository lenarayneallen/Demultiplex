# Part 3

## Wednesday, August 7th:

- Started writing python script for demultiplexing algorithm: `demulti_pt3.py`
    - location on Talapas: `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing/demulti_pt3.py`
- Had to remake test files! Original ones did not work, and I got overly confused trying to fix them, so I just started fresh. I saved them in the same place as those from part 1:
    - INPUT:
        - On talapas: `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing/INPUTTEST`
        - On my computer: `~/bioinfo/Bi621/Demultiplex/**TEST-input_FASTQ**`
        - Filenames:
            - `TEST-input_R1.fastq`
            - `TEST-input_R2.fastq`
            - `TEST-input_R3.fastq`
            - `TEST-input_R4.fastq`
    - OUTPUT:
        - On talapas: `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing/TEST-output_FASTQ`
        - On my computer:`~/bioinfo/Bi621/Demultiplex/**TEST-output_FASTQ**`
        - Filenames:
            - `GTAGCGTA-TESTOUT-R2.fastq`
            - `GTAGCGTA_TESTOUT_R1.fastq`
            - `UNK-TEST-R1.fastq`
            - `UNK-TEST-R2.fastq`
            - `HOP-R2.fastq`
            - `HOP_R1.fastq`
- Struggled with figuring out how to open file handles for all valid indexes without opening inside the loop. I ended up using a dictionary for this: `ind_filename_dict`
- Output fastq files are called:
    - Dual-Matched: `<index-index>_R1.fastq` and `<index-index>_R2.fastq`
    - Index-hopped: `hopped_R1.fastq`, `hopped_R2.fastq`
    - unknown: `unknown_R1.fastq`, `unknown_R2.fastq`
- Output summary file:
    - `index_stats.txt`
    - This summary file includes a count for EVERY OBSERVED combination of indexes (including combos with hopped indexes and combos where one or both indexes are unknown).
    - Also includes percentage reads from each sample, and total # of dual-matched, index-hopped, and unknown samples
    - Also includes percentage of index swapping

## Thursday, August 8th

- Ensured that script ran on test files! Good to go!
- Generalized script using argparse. Argparse flags listed here:
    - `-r1` : Read one fastq file
    - `-r2` : Read two fastq file
    - `-r3` : Read three fastq file
    - `-r4` : Read four fastq file
    - `-i` :  text file with indexes
    - `-qst` : quality score cutoff
- Made sure argparse worked with test files
- Wrote a **sbatch script** to run script on main files:
    - `demulti_script.sh`
    - location on Talapas: `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing/demulti_script.sh`
    
    ```bash
    #!/bin/bash
    
    #SBATCH --account=bgmp                    
    #SBATCH --partition=bgmp 
    #SBATCH --mail-user=$lenara@uoregon.edu
    
    /usr/bin/time -v ./demulti_pt3.py \
    -r1 ../../../../shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz \
    -r2 ../../../../shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz \
    -r3 ../../../../shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz \
    -r4 ../../../../shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz \
    -i  ./indexes.txt \
    -qst 30 
    ```
    
    - Job ID: 8491953
    - usr/bin/time -v output
        
        ```
        	Command being timed: "./demulti_pt3.py -r1 ../../../../shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -r2 ../../../../shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz -r3 ../../../../shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz -r4 ../../../../shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz -i ./indexes.txt -qst 30"
        	User time (seconds): 3952.70
        	System time (seconds): 73.04
        	Percent of CPU this job got: 88%
        	Elapsed (wall clock) time (h:mm:ss or m:ss): 1:15:33
        	Average shared text size (kbytes): 0
        	Average unshared data size (kbytes): 0
        	Average stack size (kbytes): 0
        	Average total size (kbytes): 0
        	Maximum resident set size (kbytes): 441476
        	Average resident set size (kbytes): 0
        	Major (requiring I/O) page faults: 0
        	Minor (reclaiming a frame) page faults: 73417
        	Voluntary context switches: 48508
        	Involuntary context switches: 12370
        	Swaps: 0
        	File system inputs: 0
        	File system outputs: 0
        	Socket messages sent: 0
        	Socket messages received: 0
        	Signals delivered: 0
        	Page size (bytes): 4096
        	Exit status: 0
        ```
        

## Friday August 9th:

- Going through my index statistics output text file, I realize that it may have been easier to have the counts for each dual-matched and index-hopped read-pair reported separate from the unknown counts. In order to make this more clear, I’m going through file and control-F-ing for each matched index pair and collecting the counts in my markdown file `Demultiplexing_report.md`
- Table for dual-matched read pairs:

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
- Also made `dual_matched.tsv` with the same columns as above excluding the index label (second column here); this is to use in making my plot!\
- python script used to make plots: `plotting.py`
    - location on Talapas: `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing/plotting.py`