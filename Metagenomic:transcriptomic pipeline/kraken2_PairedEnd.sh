#!/bin/bash


## ====================================
## user change
## ====================================
sample_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/kneaddata_out/leaf/paired/"
output_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/kraken2/leaf/paired/"
ref_db="/dev/shm/standard"
threads_num=48

## ====================================
## time recording start
## ====================================
start=$(date +%s)

## ====================================
## main loop
## ====================================
for i in `ls ${sample_dir}*_1_kneaddata_paired_1.fastq | sed 's/_1_kneaddata_paired_1.fastq//' | sed 's@/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/kneaddata_out/leaf/paired/@@'`
do

	kraken2 --db ${ref_db} --memory-mapping --threads ${threads_num} --output ${output_dir}${i}_kraken2_out.txt --report ${output_dir}${i}_kraken2_report.txt --paired ${sample_dir}${i}_1_kneaddata_paired_1.fastq ${sample_dir}${i}_1_kneaddata_paired_2.fastq

done


## ====================================
## time recording end
## ====================================
end=$(date +%s)
echo "Elapsed Time: $(($end-$start)) seconds"
