# <정수론>
# 13241
# 최소공배수
# https://www.acmicpc.net/problem/13241

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 최소공배수 = a * b // 최대공약수
def gcd(a, b):
    a, b = (a, b) if a > b else (b, a)

    while b:
        a, b = b, a % b

    return a

# 최소공배수
print(a * b // gcd(a, b))