a,b=map(int,input().split())
l=list(map(int,input().split()))
l=[[l[i],i]for i in range(a)]
l.sort()
print(l[a-1][1]+1)