import sys
a=int(input())
graph=[[]for i in range(a+2)]
ch=[0]*(a+1)

def f(n,w,lt):
    if w==0:
        zx=0
        for next in graph[n]:
            if lt!=next[0] and next[1]==1 and ch[next[0]]==0:
                f(next[0],1,n)
            if next[1]==0:zx=1
        if zx==0:ch[n]=1
    else:
        ch[n]=1
        i=0
        for next in graph[n]:
            if graph[n][i][1]==0:
                u=next[0]
                for g in range(len(graph[u])):
                    if graph[u][g][0]==n:graph[u][g][1]=2;break
                graph[n][i][1]=1
            if lt!=next[0]and ch[next[0]]==0:
                f(next[0],1,n)

            i+=1
                
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