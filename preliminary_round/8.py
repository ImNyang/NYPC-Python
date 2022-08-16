N = int(input()) # n을 입력받습니다.
res = 0 # res를 선언하고 0을 저장합니다.
visit = 0 # visit을 선언하고 0을 저장합니다.

memo = [[]for _ in range(N)] # memo에 다차원 배열을 생성합니다

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