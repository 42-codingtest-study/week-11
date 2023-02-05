import sys
input = sys.stdin.readline

t = int(input())

def gcd(a, b):
    while b != 0:
        a, b = b, (a % b)
    return a

for time in range(t):
    arr = list(map(int, input().split())) # 첫 요소는 각 케이스가 입력 받을 숫자 개수
    sum = 0
    for i in range(1, arr[0] + 1): 
        for j in range(i+1, len(arr)):
            sum += gcd(arr[i], arr[j])
    print(sum)
