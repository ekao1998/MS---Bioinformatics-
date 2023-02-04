from Bio import SeqIO #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("rosalind_splc.txt", "fasta"):
    hold_list.append(str(seq_record.seq))


DNA_Codon_Dict =  {'TTT' : 'F', "TTC": 'F', 'TTA' : 'L', 'TTG' : 'L', 'TCT' : 'S' , 'TCA' :'S', 'TCC' : 'S', 'TCG' : 'S', 'TAT' : 'Y', 'TAC': 'Y', 'TAA': 'STOP' , 'TAG': 'STOP', 'TGT' : 'C', 'TGC': 'C', 'TGA' : 'STOP', 'TGG': 'W', 'CTT' : 'L', 'CTC' : 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'CAT' : 'H', 'CAC':'H', 'CAA':'Q','CAG':'Q','CGT': 'R','CGC':'R','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ATA':'I','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GTT':'V','GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}


DNA = hold_list[0]
introns = hold_list[1:]
introns.sort(reverse=True, key=len) #cut the longest intron first, to avoid overlap, sort it in descending
#https://www.w3schools.com/python/ref_list_sort.asp
# for x in introns:
#     print(x)


for intron in introns: #this step is to remove the intron
    DNA = DNA.replace(intron,"") #https://www.w3schools.com/python/ref_string_replace.asp use replace method to remove the intron

#print(len(DNA))

for i in range(0, len(DNA)-3, 3): #-3 is bc last codon is stop codon
    print(DNA_Codon_Dict[DNA[i: i +3]],end='')

#https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/ use end='' so don't need to use ''.join method