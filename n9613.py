# <정수론>
# 9613
# GCD 합
# https://www.acmicpc.net/problem/9613

import sys
input = sys.stdin.readline

t = int(input())

def gcd(a, b):
    a, b = (a, b) if a > b else (b, a)

    while b:
        a, b = b, a % b

    return a

for _ in range(t):
    num = list(map(int, input().split()))

    n, re_num = num[0], num[1:]
    result = 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            result += gcd(re_num[i], re_num[j])

    print(result)