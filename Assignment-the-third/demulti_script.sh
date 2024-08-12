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