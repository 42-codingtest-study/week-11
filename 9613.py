# GCD 합
# https://www.acmicpc.net/problem/9613

from itertools import combinations
from math import gcd
for _ in range(int(input())) :
    lst = list(map(int, input().split()))
    n = lst.pop(0)
    answer = 0
    for i, j in combinations(lst, 2) :
        answer += gcd(i, j)
    print(answer)