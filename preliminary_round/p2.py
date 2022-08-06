map_size = int(input())

map = []

for i in map :
    for j in i:
        print("N",end=" ")
    print()

for i in range(map_size):
    tmp = input().split() # 리스트를 입력받습니다.
    num_of = list(map(str, tmp)) # 리스트로 만듭니다.
    map[i] = num_of