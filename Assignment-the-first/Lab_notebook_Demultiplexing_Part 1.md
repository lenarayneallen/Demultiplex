# Lab notebook: Demultiplexing Part 1

## Initial data exploration:

### File location on Talapas: `/projects/bgmp/shared/2017_sequencing/`

### heading the files:

- `zcat 1294_S1_L008_R1_001.fastq.gz | head`
    - appears to be biological reads - longer reads
    - **read1**
    - LENGTH
        - `zcat 1294_S1_L008_R1_001.fastq.gz | head -2 | tail -1 | wc -c`
            - length = 102 bp
    - PHRED ENCODING : 33
- `zcat 1294_S1_L008_R2_001.fastq.gz | head`
    - appears to be index reads - shorter reads
    - **index 1**
    - `zcat 1294_S1_L008_R2_001.fastq.gz | head -2 | tail -1 | wc -c`
        - length = 9 bp
    - phred encoding: 33
- `zcat 1294_S1_L008_R3_001.fastq.gz | head`
    - appears to be index reads - shorter reads
    - **index 2**
    - LENGTH
        - `zcat 1294_S1_L008_R3_001.fastq.gz | head -2 | tail -1 | wc -c`
            - length = 9 bp
    - phred encoding:  33
- `zcat 1294_S1_L008_R4_001.fastq.gz | head`
    - appears to be biological reads - longer reads
    - **read2**
    - LENGTH
        - `zcat 1294_S1_L008_R4_001.fastq.gz | head -2 | tail -1 | wc -c`
            - length = 102 bp
    - phred encoding: 33

# July 30th, 2024: Quality score analysis

## Test files

- located in file on Talapas called demultiplexing:
    - `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing`
    - `demulti_test_R<#>.fastq`

## Python Script: `qs_dist.py`

- located on Talapas at: `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing/qs_dist.py`

## Running python script

- ran 4 sbatch scripts (one for each file) simultaneously - scripts are in `/projects/bgmp/lenara/bioinfo/Bi622/demultiplexing`
    - `R1_mean.sh`
        - Job ID: 7788992
        - Node:  n0352
        
        ```bash
        #!/bin/bash
        
        #SBATCH --account=bgmp                    
        #SBATCH --partition=bgmp                  
        
        /usr/bin/time -v ./qs_dist.py \
        -f ../../../../shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz \
        -l 102 \
        -r 1
        ```
        
        ```bash
        Command being timed: "./qs_dist.py -f ../../../../shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz -l 102 -r 1"
        	User time (seconds): 8397.48
        	System time (seconds): 5.40
        	Percent of CPU this job got: 99%
        	Elapsed (wall clock) time (h:mm:ss or m:ss): 2:20:32
        	Average shared text size (kbytes): 0
        	Average unshared data size (kbytes): 0
        	Average stack size (kbytes): 0
        	Average total size (kbytes): 0
        	Maximum resident set size (kbytes): 67340
        	Average resident set size (kbytes): 0
        	Major (requiring I/O) page faults: 0
        	Minor (reclaiming a frame) page faults: 14177
        	Voluntary context switches: 816
        	Involuntary context switches: 19512
        	Swaps: 0
        	File system inputs: 0
        	File system outputs: 0
        	Socket messages sent: 0
        	Socket messages received: 0
        	Signals delivered: 0
        	Page size (bytes): 4096
        	Exit status: 0
        
        ```
        
    - `R2_mean.sh`
        - Job ID: 7788993
        - Node:  n0352
        
        ```bash
        #!/bin/bash
        
        #SBATCH --account=bgmp                    
        #SBATCH --partition=bgmp                  
        
        /usr/bin/time -v ./qs_dist.py \
        -f ../../../../shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz \
        -l 9 \
        -r 2
        ```
        
        ```bash
        Command being timed: "./qs_dist.py -f ../../../../shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz -l 9 -r 2"
        	User time (seconds): 1255.65
        	System time (seconds): 0.77
        	Percent of CPU this job got: 99%
        	Elapsed (wall clock) time (h:mm:ss or m:ss): 21:00.43
        	Average shared text size (kbytes): 0
        	Average unshared data size (kbytes): 0
        	Average stack size (kbytes): 0
        	Average total size (kbytes): 0
        	Maximum resident set size (kbytes): 60496
        	Average resident set size (kbytes): 0
        	Major (requiring I/O) page faults: 0
        	Minor (reclaiming a frame) page faults: 13856
        	Voluntary context switches: 478
        	Involuntary context switches: 3048
        	Swaps: 0
        	File system inputs: 0
        	File system outputs: 0
        	Socket messages sent: 0
        	Socket messages received: 0
        	Signals delivered: 0
        	Page size (bytes): 4096
        	Exit status: 0
        ```
        
    - `R3_mean.sh`
        - Job ID: 7788994
        - Node:  n0353
        
        ```bash
        #!/bin/bash
        
        #SBATCH --account=bgmp                    
        #SBATCH --partition=bgmp                  
        
        /usr/bin/time -v ./qs_dist.py \
        -f ../../../../shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz \
        -l 9 \
        -r 3
        ```
        
        ```bash
        Command being timed: "./qs_dist.py -f ../../../../shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz -l 9 -r 3"
        	User time (seconds): 1699.73
        	System time (seconds): 1.34
        	Percent of CPU this job got: 99%
        	Elapsed (wall clock) time (h:mm:ss or m:ss): 28:35.96
        	Average shared text size (kbytes): 0
        	Average unshared data size (kbytes): 0
        	Average stack size (kbytes): 0
        	Average total size (kbytes): 0
        	Maximum resident set size (kbytes): 60588
        	Average resident set size (kbytes): 0
        	Major (requiring I/O) page faults: 0
        	Minor (reclaiming a frame) page faults: 13414
        	Voluntary context switches: 2302
        	Involuntary context switches: 4302
        	Swaps: 0
        	File system inputs: 0
        	File system outputs: 0
        	Socket messages sent: 0
        	Socket messages received: 0
        	Signals delivered: 0
        	Page size (bytes): 4096
        	Exit status: 0
        ```
        
    - `R4_mean.sh`
        - Job ID: 7788995
        - Node:  n0352
        
        ```bash
        #!/bin/bash
        
        #SBATCH --account=bgmp                    
        #SBATCH --partition=bgmp                  
        
        /usr/bin/time -v ./qs_dist.py \
        -f ../../../../shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz \
        -l 9 \
        -r 3
        ```
        
        ```bash
        Command being timed: "./qs_dist.py -f ../../../../shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz -l 102 -r 4"
        	User time (seconds): 8509.68
        	System time (seconds): 5.64
        	Percent of CPU this job got: 99%
        	Elapsed (wall clock) time (h:mm:ss or m:ss): 2:22:21
        	Average shared text size (kbytes): 0
        	Average unshared data size (kbytes): 0
        	Average stack size (kbytes): 0
        	Average total size (kbytes): 0
        	Maximum resident set size (kbytes): 69060
        	Average resident set size (kbytes): 0
        	Major (requiring I/O) page faults: 0
        	Minor (reclaiming a frame) page faults: 14512
        	Voluntary context switches: 544
        	Involuntary context switches: 23099
        	Swaps: 0
        	File system inputs: 0
        	File system outputs: 0
        	Socket messages sent: 0
        	Socket messages received: 0
        	Signals delivered: 0
        	Page size (bytes): 4096
        	Exit status: 0
        ```
        

## how many index reads have base calls of N?

### bash commands:

`zcat 1294_S1_L008_R2_001.fastq.gz | awk 'NR % 4 == 2' | grep -c -E ".*N.*" 3976613` → 3976613

`zcat 1294_S1_L008_R3_001.fastq.gz | awk 'NR % 4 == 2' | grep -c -E ".*N.*"` → 3328051
