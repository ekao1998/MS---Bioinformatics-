#!/bin/bash


## ====================================
## user change
## ====================================
sample_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/seq_Reads/leaf/pairedEnd"
output_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/kneaddata_out/leaf/paired"
ref_db="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/refgenome/Arab_ref_TAIR10.1"
ref_db2="/student/ekao2/project/GIST/hg38"
trimmomatic_exe="/student/ekao2/miniconda3/envs/kd12/share/trimmomatic-0.39-2"
threads_num=48
bowtie2_exe="/student/ekao2/miniconda3/envs/kd12/bin"

## ====================================
## time recording start 
## ====================================
start=$(date +%s)

## ====================================
## main loop
## ====================================
for i in `ls ${sample_dir}/*_1.fastq | sed 's/_1.fastq//'`
do
	kneaddata --input1 ${i}_1.fastq  --input2 ${i}_2.fastq -o ${output_dir} -db ${ref_db} -db ${ref_db2} --trimmomatic ${trimmomatic_exe} --threads ${threads_num} --trimmomatic-options "SLIDINGWINDOW:4:15 MINLEN:36" --bowtie2 ${bowtie2_exe} 

done

## ====================================
## time recording end
## ====================================
end=$(date +%s)
echo "Elapsed Time: $(($end-$start)) seconds"
