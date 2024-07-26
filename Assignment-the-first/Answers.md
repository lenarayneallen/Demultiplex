# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz |  |  |  |
| 1294_S1_L008_R2_001.fastq.gz |  |  |  |
| 1294_S1_L008_R3_001.fastq.gz |  |  |  |
| 1294_S1_L008_R4_001.fastq.gz |  |  |  |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    2. **YOUR ANSWER HERE**
    3. **YOUR ANSWER HERE**
    
## Part 2
1. Define the problem

    The ultimate goal is to demultiplex the R1, R2, R3, and R4 fastq files. Given a table containing all 24 barcodes used in this sequencing experiment, the algorithm should iterate through each barcode. For each barcode, the algorithm should then sort through all four files record-by-record to find instances where the indexes (sequences in R2 and R3) match both each other and the current barcode. If there is a match that satisfies these conditions, the according records from R1 and R4 should each be written to a different file containing the current barcode and R1 (for R1) or R2 (for R4). When writing these records, the two barcodes themselves should be appended to the header of each record. 

    If the index sequences 1) contain any Ns in their quality scores, 2) are not in the list of 24 barcodes, or 3) have quality scores whose average is below a given threshold, the agorithm should write them to files whose titles contain "unknown" and and R1/R2. If the indexes otherwise do not match, this indicates potential index hopping, and the algorithm should write them to the files whose titles contain "hopped" and R1/R2. 

2. Describe output

    For this particular sequencing experiment, you would want the demultiplexing process to ultimately produce 52 files:

    - 48 files with matched records (2 for each of the 24 indexes)
    - 2 files for records of index hopped reads
    - 2 files for records of unknown reads

3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement

```
def ReverseComplement(seq: str) -> str:
	```Takes a sequence and returns the reverse complement of that sequence```
	return reverse_complement_of_seq
	Input: ACTG
	Expected output: CAGT
```
```
def QS_Thresh(qual_score_string: str, cutoff: int) -> bool:
	```Given a string of quality scores, Calculates the average(?) quality score of a sequence 
       and returns True if above cutoff and False if below cutoff```
    return True or False
	Input: #AAAAJJF, 70
    Expected Output: True
```
```
def Append_indexes(header: str, index1: str, index2: str) -> str
    ```Provided a header line (as a string) and two index sequences 
    (also as strings) append index sequences to header line in the following
    format: header index1-index2
    return updated_header
    Input: @K00337:83:HJKJNBBXX:8:1101:1286:1191 4:N:0:1, TACGCTAC, GTAGCGTA
    Expected Output: @K00337:83:HJKJNBBXX:8:1101:1286:1191 TACGCTAC-GTAGCGTA
```