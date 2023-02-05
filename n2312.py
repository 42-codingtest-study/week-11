import collections

n = int(input())

def factorizstion(x):
    d = 2
    number = []

    while x >= d:
        if x % d == 0:
            number.append(d)
            x /= d
        else:
            d += 1
    return number

for _ in range(n):
    x = int(input())
    number =factorizstion(x)

    dict = collections.Counter(number)

    for key in dict:
        print(key, dict[key])