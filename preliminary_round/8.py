N = int(input())
res = 0
visit = 0

memo = [[]for _ in range(N)]

for i, j in enumerate(list(map(lambda x: int(x)-1, input().split()))):
    memo[j].append(i)

for i in range(N):
    tmp = 1
    a,b = memo[i]
    for j in range(i+1, N):
        x,y = memo[j]
        tmp += ((x < a < y < b) or (a < x < b < y))
        res += tmp+1

print(res)