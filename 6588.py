# 골드바흐의 추측
# https://www.acmicpc.net/problem/6588

import sys
input = sys.stdin.readline
prime = [1] * 1000001
prime[0] = prime[1] = 0
for i in range(2, 1001) :
    if prime[i] == 1 :
        for j in range(2 * i, 1000001, i) :
            prime[j] = 0
prime_lst = [i for i in range(1000001) if prime[i] == 1]	# 처음에는 시간초과가 나왔는데, 소수들만 있는 리스트를 만들어서 돌리니까 시간초과가 없어졌다.
while 1 :
    n = int(input())
    if (n == 0) :
        break
    g = False
    for i in prime_lst :	# 여기서 소수 리스트가 없을때 백만번 돌려서 그런듯
        if prime[i] == 1 and prime[n - i] == 1 :
            print(n, "=", i, "+", n - i)
            g = True
            break
    if g == False :
        print("Goldbach's conjecture is wrong.")
