"""
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Input:
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA

ANS:
AC


"""
from Bio import SeqIO
from numpy import sort #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("rosalind_lcsm.txt", "fasta"):
    hold_list.append(str(seq_record.seq))

# print(hold_list)

# first need to sort all the seq from the shortest to the longest
sort_seq = sorted(hold_list, key = len)
# for x in sort_seq:
#     print(len(x)) 

short_seq = sort_seq[0] # the shortest in the sort_seq
remain_seq = sort_seq[1:]
motif = '' # initial the motif

for x in range(len(short_seq)): # start from the shortest's index 0
    for y in range(x,len(short_seq)): #iterate the index num
        possible = short_seq[x:y+1] #first set will be short_seq[0:1], [0:2] ..... check every possible combination
        for seq in remain_seq: #this part try to find the possible motif in every remain seq
            if possible in seq:
                pass # if found, pass, search in next seq
            else: # Once not found --> stop the search and erase the possible motif, stop the for loop
                possible = ''
                break
        if len(possible)>len(motif): # bc we want to find the longest motif so the longer one will be the new possible motif
            motif = possible

print(motif)
