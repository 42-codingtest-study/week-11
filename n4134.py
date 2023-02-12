# <정수론>
# 4134
# 다음 소수
# https://www.acmicpc.net/problem/4134

import sys
input = sys.stdin.readline

n = int(input())

''' 시간 초과
def is_prime(x):
    if x < 2:
        return False

    for i in range(2, x):   # 2부터 x - 1까지의 모든 수로 x를 나눠서
        if x % i == 0:  # 나누어 떨어지면 소수 x
            return False
    return True
'''

# 에라토스테네스의 체 사용
def is_prime(x):
    if x < 2:
        return False

    for i in range(2, int(x **0.5) + 1):
        if x % i == 0:  # 나누어 떨어지면 소수 x
            return False
    return True

for _ in range(n):
    x = int(input())

    while 1:
        if is_prime(x):
            print(x)
            break
        else:
            x += 1