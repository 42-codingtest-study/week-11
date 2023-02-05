# 다시
a, b = map(int, input().split())

if a % b == 0 or b % a == 0:
    if a > b:
        for i in range(b):
            print(1, end='')
    else:
        for i in range(a):
            print(1, end='')
else:
    print(1)