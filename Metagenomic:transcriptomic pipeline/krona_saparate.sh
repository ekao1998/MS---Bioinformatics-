#!bin/sh


cd /lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis/arab_test/kraken2/root/48_cpu

for i in `ls *.krona | sed 's/.krona//'`
do
ktImportText ${i}.krona -o ${i}.html

done

mv *.html /lab/biohpc/RNAseq_microbe_plant/ethan/arabidopsis/arab_test/krona/root
