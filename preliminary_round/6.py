N, K = map(int, input().split()) # 폭탄의 개수를 나타내는 정수(N) / 폭탄의 범위를 나타내는 정수 (K)
A = list(map(int, input().split())) # A에 list

bumpcount = N

res = 0

A.sort()

for i in range(N):
    res = res + 1
    if A[i] >= A[0]:
        if bumpcount == 0:
            break
        else:
            bumpcount -= A[i]
            res = res + 1
            del A[i]
    else:
        pass

bumpcount -= A[0] 
del A[0]

print(res)