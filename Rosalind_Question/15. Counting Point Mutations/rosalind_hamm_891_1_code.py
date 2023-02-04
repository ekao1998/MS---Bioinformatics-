import re


read1 = 'GTCTCGGGATAAGCTGCCAAAGGATAGCGCACTACGGTACTCCAGTGTTCCGTTAATGAGTATTATGGCAATAGGAAGTAGTCATCGGACAGATGAATATGTGTGTATAAGGTCCACCTCGCACTAGGCTGAGTCGCACAGCCGATTCCAATGCCTAAAGGCTCATCTTGCCCTCTAATTTCTTCAACATACGTTAGGTTGGAGAGTTCCCAGAATGTTGTACACACATTGGTAGGCGGACTCACCATTATAATGCCCTACGGCCTCTTTGCTCAGGAACATCTTGTCGGGAATTCCGGACACTCTTTCAGTCAAGGACAGTGCTACTGCCTAACCTGCCAGCATCCGTACTGTTTATGGTCGAGCATGTCTGAGTATTCCTAAGGCCCATATGATTGACCGCACCTGCCTAAACATTTGCAGGAGAAACATAAGAGTGCTAGCCTTCCAGTGAAATTTAAGACCGTGCCTGTGGAGATCCGGCTTTTGGGATGACCACATGTGAAAAACTGCGCAGGTGTTGTGCGTGTAACGTCATTTTGTCGGGACCACCGACGTATGATATTCTTTCGACGGCCGGCCAAACTTCGTCAGATCCCGGTCGATCCACCCCAGGTCTCTACACGCACATAGTGATACGGGCTTTAAGAGAGTCGTCTATAACGCCCGTGACTAATCCGTGACTTTCTCTGGGCTTATCTGGTCGGGTCAAGGCCGAGAGGTCAGACTTCAGGGCCCAGTACAATAGCAATACGGGCATCCTTTAACAGCCAAATGAAGGGTCAGTTACATGATTGCCGGCCATACAGTCGTCTTAAACCATGAGTCTGTATAAAAGCAATGTACCGGCTCCGAGACCGATCAATTTGCAGCCTGCACGACCATCCGTCATCGGGGACTGATTTTCGATCGGTGTGGGTCCTAATGAAGTTGTATTACGTAGGCCCTCGCTCCACTAGACGACGCTGTGTCCGCGTCTAAGTCT'
read2 = 'GTTTTGCGTTAAGGTGAGAAGGAGTAGGCCCCAACCGTGGGCCGGTAGTAGCTTAAACATGAATAAGATCACAGGGAGACAACCTTGTACTGAAGTACGCCGACCACTAAGGTCCCCCGGGGGCTCGGCGGAATTACGCCATGGTACCGAACTAATCTAAATTCATCTTCCCTTACTACACGCACTGATGGGGTCGGGTCGTATTCGTGCCTGTTTGTGGTGTAAAGTTGCACGGAGTGTCGCGACATTGGTCATCTGGACCGACAAGCGCATCAGGTTCATTTTTTCGCGTTGAACGCTATCCGTTTCAGGGCATCAAGTTGGTCCAACATATAATCCAGGTCGTCCCCCGAGTAAGGGACTGGCCTCACCAAGTATCGCGAAGGTTTCGGTAATTTCGTGAGCTTGATCAACCATTTGGAGTGGGACCACCTCGGACCTAGCCTTCATGAATAATACAAAATCGTGCGTCTCACAATTACCCCAGTCTAGGCCCCACTTGTAGGAATCTGCGCCCCCGTTCGGATTGCATTGTCTCGTTCGTAGAGCCTCCGACGTTTAAGTGATTCGAGATAACTTTGGATATGGCCCCCGCATACGCTCTCTCGGTTCTACTTCATTAGACAGAAATAATGTGACCAGCATAGACTGTGCCTCCCATAATTATAGGAACAGAGATAGGACTTTGGTTGGGGTGAGTTTTAAGGGGAACCTTCGAGAACACAGGCTTCCGGAGGCGGTACATCGCCCTATCTGACCTGTCCTGGCCACGTGATGTAGACTAATGTACAGCAAAACCACCCAGGCCGTACGCGGAATCGATAGGTTTGCATAAAAGTTATTGGATGCATCTTGGTCGAGACCAGCAGCTGCCCGATCTACGCAACTACACCATGGATAAGATTTCCTTGATTGTGGGTCTTAGCCACGATGGATGTAAAGGGTCTTCGCCGCATTAGCTGACTATGTCGCCGGCCCTCAGTCT'
count=0
for k in range(len(read1)):
    if read1[k] != read2[k]:
        count+=1
print(count)