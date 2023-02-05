# 보이는 점의 개수
# https://www.acmicpc.net/problem/2725

# 최대공약수가 1인 친구가 원점에서 보이는 점이다. 1이 아니면 보이지 않는 점임
import sys
input = sys.stdin.readline
def gcd(i, j):
    if j == 0:
        return i
    return gcd(j, i % j)

dp = [0 for _ in range(1001)]
dp[1] = 3
for i in range(2, 1001):
    cnt = 0
    for j in range(1, i+1):
        if i == j:
            continue
        if gcd(i, j) == 1:
            cnt += 2
    dp[i] = dp[i-1] + cnt

for _ in range(int(input())):
    N = int(input())
    print(dp[N])