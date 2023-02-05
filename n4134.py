import math

n = int(input())

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(n):
    x = int(input())

    while 1:
        if is_prime(x):
            print(x)
            break
        else:
            x += 1

