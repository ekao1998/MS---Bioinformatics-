#!/bin/sh


## ====================================
## user change
## ====================================
sample_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/kraken2/leaf/single/"
output_dir="/lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis_Ethan/arab_test_100_sample_v2/krona/leaf/"
combine_kreports="/public/ahnt/software/KrakenTools/combine_kreports.py"
kreport2krona="/public/ahnt/software/KrakenTools/kreport2krona.py"
filename="All_leaf_singleEnd_MinLen36"

## ====================================
## main loop
## ====================================
${combine_kreports} -r ${sample_dir}*_kraken2_report.txt -o ${sample_dir}${filename}_kraken2.report

${kreport2krona} -r ${sample_dir}${filename}_kraken2.report -o ${sample_dir}${filename}_kraken2.krona

ktImportText ${sample_dir}${filename}_kraken2.krona -o ${output_dir}${filename}.html

