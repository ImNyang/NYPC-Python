import sys,math # sys와 math 라이브러리를 불러옵니다.
sys.setrecursionlimit(10**9)
inf=math.inf
input=sys.stdin.readline
a=int(input())
l=[list(map(int,input().split()))for i in range(a)]
for i in range(a):l[i].append(i)
l.sort(reverse=True)
l+=[[0,-inf,inf,0,0]]
ans=[0]*(a+2)
ch=[inf]*(a+2)
def f(x,last):
    print(x,last,i)
    if ch[x]!=inf:return ch[x]
    if x+1==a+1:return 0
    mi=inf
    if l[x][1]<=l[a][1]<=l[x][2]or l[x][1]<=l[a][2]<=l[x][2]or l[a][1]<=l[x][1]<=l[a][2]or l[a][1]<=l[x][2]<=l[a][2]:
        mi=(l[x][0]-l[a][0])**2+l[a][0]
    for ix in range(x+1,a):
        ty=inf
        io=f(ix,x)
        if l[x][1]<=l[ix][1]<=l[x][2]or l[x][1]<=l[ix][2]<=l[x][2]or l[ix][1]<=l[x][1]<=l[ix][2]or l[ix][1]<=l[x][2]<=l[ix][2]:
            ty=(l[x][0]-l[ix][0])**2+l[ix][3]
        io+=ty
        mi=min(mi,io)
    ch[x]=mi
    ans[l[x][4]]=mi
    return mi
f(0,-1)

for i in range(a):
    print(ans[i])