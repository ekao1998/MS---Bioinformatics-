"""
For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

Input:
>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT

ANS:
1.21428571429


"""
from Bio import SeqIO #import the biopython 
hold_list=[]
for seq_record in SeqIO.parse("rosalind_tran.txt", "fasta"):
    hold_list.append(str(seq_record.seq))


R1 = hold_list[0]
R2 = hold_list[1]
Transition_count = 0
Transversion_count = 0
for x in range(len(R2)):
    pair = R1[x],R2[x]
    if pair in [('A', 'G'),('G', 'A'), ('C', 'T'), ('T', 'C')]:
        Transition_count+=1
    elif pair in [('A', 'A'),('G', 'G'), ('C', 'C'), ('T', 'T')]:
        pass
    else:
        Transversion_count+=1


transition_transversion_ratio = Transition_count / Transversion_count
print(transition_transversion_ratio)
    