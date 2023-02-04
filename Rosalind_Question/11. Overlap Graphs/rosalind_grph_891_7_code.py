from copy import copy
from Bio import SeqIO #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("rosalind_grph_891_7_dataset.txt", "fasta"):
    hold_list.append([seq_record.id,seq_record.seq[:3],seq_record.seq[-3::]])


hold_name = ''
hold_front = ''
hold_end = ''

for k in hold_list:
    compare_list = copy(hold_list)
    hold_name = k[0] 
    hold_front = k[1]
    hold_end = k[2]
    compare_list.remove(k) #remove first [set] in the hold_list
    
    for l in compare_list: #and compare the rest of the list to the hold( name, front ,end )

        if hold_end ==l[1]:
            print(hold_name +' '+l[0])