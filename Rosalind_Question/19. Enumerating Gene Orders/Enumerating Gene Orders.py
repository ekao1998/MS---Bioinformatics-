import itertools as it
##https://docs.python.org/3/library/itertools.html#itertools.permutations

#### turn num to ordering of the positive integers {1,2,…,n}
num=5
holdList=[]
for k in range(1,num+1):
    holdList.append(str(k))

String = "".join(holdList)


####formatting
count=0
for i in it.permutations(String):
    count+=1
print(count)

for i in it.permutations(String):
    print(' '.join(i))

