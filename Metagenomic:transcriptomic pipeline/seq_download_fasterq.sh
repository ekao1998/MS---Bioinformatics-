#!/bin/sh

## ====================================
## user change
## ====================================
Sra_AccList_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/seq_Reads/leaf/pairedEnd/"
Sra_AccList_name="leaf_paired_copy.txt"

## ====================================
## time recording start 
## ====================================
start=$(date +%s)

## ====================================
## main loop
## ====================================
while read line; do fasterq-dump --threads 48 -O ${Sra_AccList_dir} $line; done < ${Sra_AccList_dir}${Sra_AccList_name}

## ====================================
## time recording end
## ====================================
end=$(date +%s)
echo "Elapsed Time: $(($end-$start)) seconds"
