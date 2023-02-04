"""
A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.

Input:
>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA

ANS:
3 8 10


"""
from Bio import SeqIO #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("rosalind_sseq.txt", "fasta"):
    hold_list.append(str(seq_record.seq))

Sequence = hold_list[0]
SubSeq = hold_list[1]

Index = []
index_hold = -1 #initial to -1, no index can be smaller then this

for char in list(SubSeq):
    found = False
    count = 0 #start searching from first latter in the Sequence
    while not found: #running until found the proper index 
        if Sequence.index(char,count)>index_hold: 
            index_hold = Sequence.index(char,count) #update index hold, so not latter need to be bigger than this to mean the criteria
            Index.append(Sequence.index(char,count))
            found = True #if found stop the loop
        else:
            count+=1 


##Index num change to Indice need to add one
for num in Index:
    num +=1
    print(num, end=" ")
