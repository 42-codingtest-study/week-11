a, b = map(int,input().split())
m = int(input())
arr = list(map(int,input().split()))


arr.reverse()
originNum = 0
for i in range(m):
    originNum += arr[i] * (a ** i)

res = []
while (originNum // b) :
    res.append(originNum % b)
    originNum = originNum // b
res.append(originNum)

print(*res[::-1])
