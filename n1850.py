# <정수론>
# 1850
# 최대공약수
# https://www.acmicpc.net/problem/1850

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

# 유클리드 호제법 사용 -? 왜
def gcd(x, y):

    if x < y:
        x, y = y, x

    while y:
        x, y= y, x % y

    return x

print('1' * gcd(a, b))