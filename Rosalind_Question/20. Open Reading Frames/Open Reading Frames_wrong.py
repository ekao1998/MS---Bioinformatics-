from Bio.Seq import Seq
DNA = Seq("AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG")
DNA_reverse_complement = str(DNA.reverse_complement())


n = 3 #codon --> 3 character
Codon=[]

for x in range(3): #forward RF
    temp=[]
    for i in range(x, len(DNA), n):
        temp.append(str(DNA)[i:i+n])
    Codon.append(temp)
 
for x in range(3): #Reverse RF
    temp=[]
    for i in range(x, len(DNA_reverse_complement), n):
        temp.append(DNA_reverse_complement[i:i+n])
    Codon.append(temp)


Protein=[]
for x in Codon:
    temp=[]
    count=0
    for i in x:
        if i in ["TTT","TTC"]:
            if count>0:
                temp.append("F")

        elif i in ["TTA","TTG","CTT","CTC","CTA","CTG"]:
            if count>0:
                temp.append("L")

        elif i in ["TCT","TCC","TCA","TCG","AGT","AGC"]:
            if count>0:
                temp.append("S")

        elif i in ["TAT","TAC"]:
            if count>0:
                temp.append("Y")

        elif i in ["TAA","TAG","TGA"]:
            if count>0:
                temp.append("q")

        elif i in ["TGT","TGC"]:
            if count>0:
                temp.append("C")

        elif i in "TGG":
            if count>0:
                temp.append("W")

        elif i in ["CCT","CCC","CCA","CCG"]:
            if count>0:
                temp.append("P")

        elif i in ["CAT","CAC"]:
            if count>0:
                temp.append("H")

        elif i in ["CAA","CAG"]:
            if count>0:
                temp.append("Q")

        elif i in ["CGT","CGC","CGA","CGG","AGA","AGG"]:
            if count>0:
                temp.append("R")

        elif i in ["ATT","ATC","ATA"]:
            if count>0:
                temp.append("I")

        elif i in "ATG":
            count+=1
            temp.append("M") 

        elif i in ["ACT","ACC","ACA","ACG"]:
            if count>0:
                temp.append("T")

        elif i in ["AAT","AAC"]:
            if count>0:
                temp.append("N")

        elif i in ["AAA","AAG"]:
            if count>0:
                temp.append("K")
        
        elif i in ["GTT","GTC","GTA","GTG"]:
            if count>0:
                temp.append("V")
        
        elif i in ["GCT","GCC","GCA","GCG"]:
            if count>0:
                temp.append("A")

        elif i in ["GAT","GAC"]:
            if count>0:
                temp.append("D")

        elif i in ["GAA","GAG"]:
            if count>0:
                temp.append("E")

        elif i in ["GGT","GGC","GGA","GGG"]:
            if count>0:
                temp.append("G")
    Protein.append(temp)


ANS=[] #protein seq from 6 RF
for x in Protein:
    ans = "".join(x)
    ANS.append(ans)
a=ANS[0]
found = False
while not found:
    temp = []
    n=0
    count = 0
    if a[n] =="M":
        count+=1
        temp.append(a[n])
        n+=1
        
    else:
        n+=1

# for seq in ANS: #here we need to check if there are more than one M in the Protein seq, if so it will be another seq
#     if seq.count("M")>1: 
#         n=seq.count("M") # count how many M a seq have 
#         for x in range(2,n+1):
#             ANS.append(seq[seq.index("M",n):]) #start from specific M

# for i in ANS:
#     print(i)


    
    
