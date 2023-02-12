# <정수론>
# 11576
# Base Conversion
# https://www.acmicpc.net/problem/11576

import sys
input = sys.stdin.readline

a, b = map(int, input().split())    # a: 미래 진법, b: 정이가 쓰는 진법

m = int(input())    # a진법 자리수
number = list(map(int, input().split()))    # a진법 숫자들

numberA = 0    # a진법 숫자 -> 10진법 변환한 숫자

# 첫째자리부터 계산해야 하기 때문에 number 역순으로 정렬
number.reverse()

for i in range(m):
    numberA += number[i] * (a ** i)

# 숫자 b진법으로 표시하기
# : 숫자를 b로 나누어 그 나머지를 표시하고 더 이상 나눌 수 없을때까지 반복
numberB = []    # b진법 숫자

while numberA // b != 0:    # 더 이상 나누지지 않을 때까지
    numberB.append(numberA % b)
    numberA //= b

numberB.append(numberA)

# b진법 숫자를 큰 자리수부터 출력해야 하므로 역순으로 정렬
numberB.reverse()

for i in numberB:
    print(i, end=' ')