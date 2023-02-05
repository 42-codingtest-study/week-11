a, b = map(int, input().split())

# 최대공약수 - 유클리드 호제법
def gcd(a, b):
    while b:
        mod = b
        b = a % b
        a = mod
    return a

# 최소공배수
print(a * b // gcd(a, b))