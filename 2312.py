# 수 복원하기
# https://www.acmicpc.net/problem/2312

import sys
input = sys.stdin.readline
for _ in range(int(input())) :
    n = int(input())
    for i in range(2, n + 1) :
        cnt = 0
        if n % i == 0 :
            while n % i == 0 :
                n //= i
                cnt += 1
            print(i, cnt)
        elif n == 1 :
            break