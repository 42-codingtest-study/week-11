import math

t = int(input())

for _ in range(t):
    arr = list(map(int, input().split()))

    result = 0

    for i in range(1, len(arr)):
        for j in range(i + 1, len(arr)):
            result += math.gcd(arr[i], arr[j])

    print(result)