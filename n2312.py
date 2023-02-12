# <정수론>
# 2312
# 수 복원하기
# https://www.acmicpc.net/problem/2312

import sys
input = sys.stdin.readline

n = int(input())

def factorizstion(x):
    d = 2
    number = []

    while x >= d:
        if x % d == 0:
            number.append(d)
            x /= d
        else:
            d += 1
    return number


for _ in range(n):
    x = int(input())
    x_number = factorizstion(x)   # x 소인수분해 한 결과 저장

    d = {}

    for i in x_number:
        d[i] = d.get(i, 0) + 1

    for key in d:
        print(key, d[key])