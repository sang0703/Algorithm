# 문제 https://www.acmicpc.net/problem/3003

chess = [1, 1, 2, 2, 2, 8]
c = list(map(int, input().split())) 
for i in range(6):
    print(chess[i] - c[i], end=' ')
