"""
Assume that an alphabet š has a predetermined order; that is, we write the alphabet as a permutation š=(a1,a2,ā¦,ak), where a1<a2<āÆ<ak. For instance, the English alphabet is organized as (A,B,ā¦,Z).

Given two strings s and t having the same length n, we say that s precedes t in the lexicographic order (and write s<Lext) if the first symbol s[j] that doesn't match t[j] satisfies sj<tj in š.

Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (nā¤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).


Input:
A C G T
2


Ans:
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT


ref: https://docs.python.org/3/library/itertools.html
"""

from itertools import product

input = 'ABCD'
repeat_input = 4

ans = list(product(input, repeat = repeat_input))

for x in ans:
    print(''.join(x))