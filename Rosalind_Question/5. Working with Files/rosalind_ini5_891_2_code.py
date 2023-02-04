with open('rosalind_ini5.txt') as f:
    contents=f.readlines()
    odd=1
    while odd <= len(contents):
        print(contents[odd].strip('\n'))
        odd+=2