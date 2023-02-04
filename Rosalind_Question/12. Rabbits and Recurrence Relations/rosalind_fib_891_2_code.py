def countRabbit(n,k):
    parent = 1
    child = 1
    for i in range(n-2):
        child, parent = parent, parent + child * k
        #print(child)
        #print(str(parent)+"\n")
    return parent





print(countRabbit(36,5))
"""


1: m -->skip this line
2: M     1 c
3: Mmmm  4 p  4 c
4: Mmmm MMM   7 p            7  c
5: Mmmm MMM Mmmm Mmmm Mmmm   19 p

3sets --> n-2
"""