# 최대공약수
# https://www.acmicpc.net/problem/1850

def gcd(x, y) :
    mod = x % y
    while mod > 0 :
        x = y
        y = mod
        mod = x % y
    return y

A, B = map(int, input().split())
print('1' * gcd(A, B))
