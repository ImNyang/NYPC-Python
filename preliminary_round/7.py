N = int(input())

tree = []
for i in range(N-1): # i에 1을 계속 더하며 0~N-2이 될때까지 반복합니다.
    templist = list(map(int, input().split())) # templist로 나무의 한줄을 받습니다.
    tree.append(templist) # tre에 templist의 리스트를 추가합니다.
