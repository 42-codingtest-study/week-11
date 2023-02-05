a, b = map(int, input().split())
n = int(input())

arr = list(map(int, input().split()))
# 첫째자리부터 계산해야함
arr.reverse()
number = 0 # 10진수 변환 값

for i in range(n):
    number += arr[i] * (a ** i)

result = []

while number // b != 0:
    result.append(number % b)
    number = number // b

result.append(number)
result.reverse()

for i in result:
    print(i, end=' ')