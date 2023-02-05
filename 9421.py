# 소수상근수
# https://www.acmicpc.net/problem/9421

import sys
sys.setrecursionlimit(10 ** 7)
n = int(input())
prime = [True] * (n + 1)
prime[0] = prime[1] = False
for i in range(2, int(n ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, n + 1, i) :
            prime[j] = False
prime_lst = [i for i in range(n + 1) if prime[i]]
def fn(n, ov) :
    s = 0
    for i in list(str(n)) :
        s += int(i) ** 2
    if s == 1 :
        return True
    elif s in ov :
        return False
    else :
        ov.add(s)
        return fn(s, ov)
for i in prime_lst :
    if fn(i, set()) :
        print(i)