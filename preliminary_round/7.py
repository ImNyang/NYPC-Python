import sys # sys 라이브러리를 불러옵니다.
a=int(input()) # a를 입력받고 저장합니다.
graph=[[]for i in range(a+2)] # graph에 2차원 배열을 생성합니다.
ch=[0]*(a+1) # ch에[0] a+1을 곱한다. 

def f(n,w,lt): # f라는 함수를 만든뒤 n,w,lt를 받는다
    if w==0: #만약 w가 0이라면
        zx=0 # zx를 0으로 선언합니다.
        for next in graph[n]: #next에 graph[n]을 넣습니다. 그리고 반복합ㄴ디ㅏ.
            if lt!=next[0] and next[1]==1 and ch[next[0]]==0:
                f(next[0],1,n) # f함수를 불러옵니다. 값 : n = next[0] / w = 1 / lt = n
            if next[1]==0:zx=1 #next[1]이 0이라면...        zx를 1로 만듭니다.
        if zx==0:ch[n]=1 # zx가 0이라면...      ch[n]을 1로 만듭니다.
    else: # 아니라면...
        ch[n]=1 # ch[n]을 1로 만듭니다.
        i=0 # i를 0으로 만듭니다.
        for next in graph[n]: # next에 graph[n]을 집어넣고 반복합니다.
            if graph[n][i][1]==0: # 다차원 배열인 graph[n][i][1]가 0이라면...
                u=next[0] # u를 next[0]으로 정합니다.
                for g in range(len(graph[u])): # g에 1을 계속 더하며 0~(graph[u]의 글자수)-1이 될때까지 반복합니다.
                    if graph[u][g][0]==n:graph[u][g][1]=2;break # 만약 graph[u][g][0]이 n이라면 graph[u][g][1]을 2로 정하고 이 함수를 끝낸다.
                graph[n][i][1]=1 # graph[n][i][1]를 1로 정합니다.
            if lt!=next[0]and ch[next[0]]==0: # 만약 lt이 next[0]이 아니고 ch[next[0]]이 0이라면...
                f(next[0],1,n) # f함수를 불러옵니다. 값 : n = next[0] / w = 1 / lt = n
            i+=1 # i에 1을 더합니다.
                
# 아래는 알아서...

for i in range(a-1):
    b,c,d=map(int,input().split())
    graph[b].append([c,d])
    if d==0:
        graph[c].append([b,d])
#print(graph)
for i in range(1,a+1):
    if ch[i]==0:
        f(i,0,-1)
#print(graph)
st=[0]*(a+1)
for i in range(1,a+1):
    for g in range(len(graph[i])):
        if graph[i][g][1]==1:
            st[graph[i][g][0]]+=1
            if st[graph[i][g][0]]>=2:
                print(0)
                sys.exit()
#print(st)
ans=0
for i in range(1,a+1):
    if st[i]==0:
        ans+=1
print(ans)