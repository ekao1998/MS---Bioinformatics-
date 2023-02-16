#!bin/sh

cd /lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis/arab_test/kraken2/root/48_cpu

for i in `ls *_kraken2_report.txt | sed 's/_kraken2_report.txt//'`
do
/public/ahnt/software/KrakenTools/kreport2krona.py -r ${i}_kraken2_report.txt -o ${i}.krona

done
