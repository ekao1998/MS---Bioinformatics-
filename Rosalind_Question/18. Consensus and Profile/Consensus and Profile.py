from Bio import SeqIO

holdSeq=[] 
for record in SeqIO.parse("rosalind_cons.txt", "fasta"):
    holdSeq.append(record.seq)



index = len(holdSeq[0])
A=[]
T=[]
C=[]
G=[]

######### build_profile
for k in range(index): 
    A_count=0
    T_count=0
    C_count=0
    G_count=0
    for seq in holdSeq: #iterate every seq
        if seq[k] == "A":
            A_count+=1
        elif seq[k] == "T":
            T_count+=1
        elif seq[k] == "C":
            C_count+=1
        elif seq[k] == "G":
            G_count+=1
    A.append(str(A_count))
    T.append(str(T_count))
    C.append(str(C_count))
    G.append(str(G_count))

######### build_consensus

profileHold = [] #in A,T,C,G order
profileHold.append(A)
profileHold.append(T)
profileHold.append(C)
profileHold.append(G)

seqLen = len(holdSeq[0])
Consensus=[]
for i in range(seqLen): #this step is to iterate the index
    hold=[]
    for profileNum in profileHold: #in A,T,C,G order 
        hold.append(int(profileNum[i]))

    if hold.index(max(hold)) == 0: 
        Consensus.append("A")
        
    elif hold.index(max(hold)) == 1: 
        Consensus.append("T")

    elif hold.index(max(hold)) == 2: 
        Consensus.append("C")  

    elif hold.index(max(hold)) == 3: 
        Consensus.append("G")

  
       
  

######### formatting

joinConsensus = "".join(Consensus)
joinA = " ".join(A)
joinT = " ".join(T)
joinC = " ".join(C)
joinG = " ".join(G)

print(joinConsensus)
print("A: " + joinA)
print("C: " + joinC)
print("G: " + joinG)
print("T: " + joinT)