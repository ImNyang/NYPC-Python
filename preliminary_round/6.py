from queue import PriorityQueue

N,K=map(int,input().split())
l=list (map(int,input().split()))

que=PriorityQueue()
for i in range(N):que.put([l[i],i])

st=[0]*(N+1)
ch=0
cnt=N
ans=0

while ch!=N and cnt!=0:
    s=que.get()
    cnt-=1
    if st[s[1]]==0:
        ans+=1
        left=s[1]-1
        right=s[1]+1
        st[s[1]]=1
        while left>=0 and st[left]==0 and s[0]<=l[left]<=s[0]+K:ch+=1;st[left]=1;left-=1
        while right<N and st[right]==0 and s[0]<=l[right]<=s[0]+K:ch+=1;st[right]=1;right+=1

print(ans)