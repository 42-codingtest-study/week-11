import sys 
input = sys.stdin.readline

def solve(n):
    while 1:
        t = 1
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                n += 2
                t = 0
                break
        if t:
            return n
    

for _ in range(int(input())):
    n = int(input())
    if n <= 2:
        print(2)
    else:
        if n % 2 == 0:
            n += 1
        print(solve(n))