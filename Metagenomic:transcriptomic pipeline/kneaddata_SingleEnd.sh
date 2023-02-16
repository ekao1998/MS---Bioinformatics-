#!/bin/bash


## ====================================
## user change
## ====================================
sample_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/seq_Reads/root/singleEnd"
output_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/kneaddata_out/root/single"
ref_db="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/refgenome/Arab_ref_TAIR10.1"
ref_db2="/student/ekao2/project/GIST/hg38"
trimmomatic_exe="/student/ekao2/miniconda3/envs/kd12/share/trimmomatic-0.39-2"
threads_num=32
bowtie2_exe="/student/ekao2/miniconda3/envs/kd12/bin"

## ====================================
## time recording start 
## ====================================
start=$(date +%s)

## ====================================
## main loop
## ====================================
for i in `ls ${sample_dir}/*.fastq | sed 's/.fastq//'`
do
	kneaddata -un ${i}.fastq -o ${output_dir} -db ${ref_db} -db ${ref_db2} --trimmomatic ${trimmomatic_exe} --threads ${threads_num} --trimmomatic-options "SLIDINGWINDOW:4:15 MINLEN:36" --bowtie2 ${bowtie2_exe} 

done

## ====================================
## time recording end
## ====================================
end=$(date +%s)
echo "Elapsed Time: $(($end-$start)) seconds"
