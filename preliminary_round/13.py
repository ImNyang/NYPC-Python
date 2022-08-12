a,b=map(int,input().split()) # int형 2가지를 입력받습니다. 그리고 받은 값을 a와 b에 저장합니다.
l=list(map(int,input().split())) # int형 여러가지를 입력받습니다. 그리고 받은 int형 값을 list로 저장합니다.
l=[[l[i],i]for i in range(a)] # 2차원 배열을 만듭니다.
l.sort() # list를 정렬합니다.
print(l[a-1][1]+1) # l[a-1][1]+1을 출력합니다.