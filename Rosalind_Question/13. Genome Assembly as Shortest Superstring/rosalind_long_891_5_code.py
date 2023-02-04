from Bio import SeqIO

holdSeq=[] #At most 50 DNA strings of approximately equal length
for record in SeqIO.parse("rosalind_long_891_5_dataset.txt", "fasta"):
    holdSeq.append(record.seq)


Pin = StartAssembly = holdSeq[0] #At most 50 DNA strings of approximately equal length, so can start from any string

# gluing together pairs of reads that overlap by more than half their length. 
k = len(holdSeq[0])//2 + 1    

####break into two parts:

####First, check the all possible overlap with TailPin and update to the Pin

for i in range(1000): #don't know how many run it will take. a random number
    currentPin = Pin 
    for EstimateOverlapLen in range(k,len(holdSeq[0])): #At least half overlap
        for seq in holdSeq[1:]: #compare the Pin to other seq in the holdSeq, the overlap len will +1 over iteration to almost 1k
            Tail_Pin = Pin[-EstimateOverlapLen:]
            Head_Otherseq = seq[:EstimateOverlapLen]
            if Tail_Pin == Head_Otherseq:
                Pin = Pin + seq[EstimateOverlapLen:] #add the rest part of the Otherseq
    if currentPin == Pin: #if Pin stop update, than break
        break

####Second, check the all possible overlap with HeadPin and update to the Pin

for i in range(1000): #don't know how many run it will take. a random number
    currentPin = Pin
    for EstimateOverlapLen in range(k,len(holdSeq[0])): #At least half overlap, the overlap len will +1 over iteration,to almost 1k
        for seq in holdSeq[1:]: #compare the Pin to other seq in the holdSeq
            Head_Pin = Pin[:EstimateOverlapLen]
            Tail_Otherseq = seq[-EstimateOverlapLen:]
            if Head_Pin == Tail_Otherseq:
                Pin = seq + Pin[EstimateOverlapLen:]  #add the rest part of the Otherseq
    if currentPin == Pin: #if Pin stop update, than break
        break


print(Pin)