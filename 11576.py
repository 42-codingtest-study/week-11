# Base Conversion
# https://www.acmicpc.net/problem/11576

A, B = map(int, input().split())
m = int(input())
m_lst = list(map(int, input().split()))
conv = 0
for i in range(len(m_lst) - 1, -1, -1) :
    conv += (A ** (len(m_lst) - 1 - i)) * m_lst[i]
answer = []
while conv >= B :
    answer.append(conv % B)
    conv //= B
answer.append(conv)
for i in range(len(answer) - 1, -1, -1) :
    print(answer[i], end = ' ')