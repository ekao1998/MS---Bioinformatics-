from Bio import SeqIO #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("rosalind_gc_891_2_dataset.txt", "fasta"):
    hold_list.append([seq_record.id,(seq_record.seq.count('C') + seq_record.seq.count('G'))/len(seq_record)*100])
#in this for loop append a list [inculde the name and the GC content in % ] to the hold_list

max=0.0
for k in hold_list: 
    if k[1]>max:
        max=k[1]
#run through the hold_list to find the max GC content

name=''
for l in hold_list:
    if max in l:
        name = l[0]
#when the max num find, go back and find the name

print(name)
print(max)