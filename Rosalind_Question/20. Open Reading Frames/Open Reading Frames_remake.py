from Bio import SeqIO  #read fasta file
from Bio.Seq import Seq #reverse complement
hold_list=[]
for seq_record in SeqIO.parse("rosalind_orf.txt", "fasta"):
    hold_list.append(str(seq_record.seq))

DNA = hold_list[0]
DNA_Codon_Dict =  {'TTT' : 'F', "TTC": 'F', 'TTA' : 'L', 'TTG' : 'L', 'TCT' : 'S' , 'TCA' :'S', 'TCC' : 'S', 'TCG' : 'S', 'TAT' : 'Y', 'TAC': 'Y', 'TAA': 'STOP' , 'TAG': 'STOP', 'TGT' : 'C', 'TGC': 'C', 'TGA' : 'STOP', 'TGG': 'W', 'CTT' : 'L', 'CTC' : 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC' : 'P', 'CCA' : 'P', 'CCG' : 'P', 'CAT' : 'H', 'CAC':'H', 'CAA':'Q','CAG':'Q','CGT': 'R','CGC':'R','CGA':'R','CGG':'R','ATT':'I','ATC':'I','ATA':'I','ATG':'M','ACT':'T','ACC':'T','ACA':'T','ACG':'T','AAT':'N','AAC':'N','AAA':'K','AAG':'K','AGT':'S','AGC':'S','AGA':'R','AGG':'R','GTT':'V','GTC':'V','GTA':'V','GTG':'V','GCT':'A','GCC':'A','GCA':'A','GCG':'A','GAT':'D','GAC':'D','GAA':'E','GAG':'E','GGT':'G','GGC':'G','GGA':'G','GGG':'G'}



DNA = Seq(DNA)
DNA_reverse_complement = str(DNA.reverse_complement())
#print(len(DNA))
# print(DNA)
# print(DNA_reverse_complement)


answer=[]

for i in range(len(DNA)-2): #-2 let next line can iterate through all the codon
    #print(i)
    if DNA[i:i+3]=='ATG': #to find ATG
        j=i
        protein=''
        letter='ATG'
        while DNA_Codon_Dict[letter]!="STOP":
            protein+=DNA_Codon_Dict[letter]
            j+=3           #shift to next codon, until reach the stop codon while loop condition
            if j>len(DNA)-3:
                break     #or j>seq len, will stop 
            letter=DNA[j:j+3]
        if DNA_Codon_Dict[letter]=="STOP" and protein not in answer:
            answer.append(protein)

for i in range(len(DNA_reverse_complement)-2):
    if DNA_reverse_complement[i:i+3]=='ATG':
        j=i
        protein=''
        letter='ATG'
        while DNA_Codon_Dict[letter]!="STOP":
            protein+=DNA_Codon_Dict[letter]
            j+=3
            if j>len(DNA_reverse_complement)-3:
                break
            letter=DNA_reverse_complement[j:j+3]
        if DNA_Codon_Dict[letter]=="STOP" and protein not in answer:
            answer.append(protein)

for i in answer:
    print(i)
    