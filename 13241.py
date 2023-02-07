# 최소공배수
# https://www.acmicpc.net/problem/13241

from math import gcd
A, B = map(int, input().split())
print(A * B // gcd(A, B))