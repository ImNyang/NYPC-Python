import math

def main():
    a = None
    b = None
    c = None
    mi = None
    cnt = None
    ans = 0
    n,m = map(int, input().split())
    for i in range(1, n + 1):
        arr[i] = map(int, input().split())
        Globals.update(1, i, 1, n, arr[i])
    Globals.srt(1, 1, n)
    for i in range(2, m + 1):
        ans+=Globals.get(1, 1, n, 1, i, arr[i])
    ma = ans
    #printf("%lld\n",ans)
    for i in range(m+1, n + 1):
        A = Globals.get(1, 1, n, i-m+1, i-1, arr[i])
        B = Globals.get(1, 1, n, i-m, i-1, arr[i-m])
        ans+=A
        ans-=B
        ma = max(ma,ans)
        #printf("%lld %lld %lld\n",ans,A,B)
    print("{0:d}\n".format(ma), end = '')



class Globals:
    # C++

    tree = [[] for _ in range(800010)]
    sutree = [[] for _ in range(800010)]
#C++ TO PYTHON CONVERTER TODO TASK: The following statement was not recognized, possibly due to an unrecognized macro:
    list<long> arr(200002)
    asd = 0
    @staticmethod
    def update(bucket, node, start, end, x):
        if node<start or end<node:
            return
        Globals.tree[bucket].append(x)
        if start != end:
            Globals.update(bucket *2, node, start, math.trunc((start+end) / float(2)), x)
            Globals.update(bucket *2+1, node, math.trunc((start+end) / float(2))+1, end, x)

    @staticmethod
    def get(node, start, end, left, right, x):
        if left> end or right<start:
            return 0
        if left<=start and end<=right:
            jk = Globals.tree[node].end()-upper_bound(Globals.tree[node].begin(),Globals.tree[node].end(),x)
            #printf("%lld %lld %lld %lld\n",start,end,jk,sutree[node][end-start+1])
            kp = end-start+1
            pit = ((Globals.sutree[node][kp]-Globals.sutree[node][kp-jk])-(x *jk))+((x*(kp-jk))-Globals.sutree[node][kp-jk])
            return pit
            #return jk
        mid = math.trunc((start+end) / float(2))
        return Globals.get(node *2, start, mid, left, right, x) + Globals.get(node *2+1, mid+1, end, left, right, x)
    @staticmethod
    def srt(node, start, end):
        sort(Globals.tree[node].begin(),Globals.tree[node].end())
        Globals.sutree[node].append(0)
        io = 0
        while io<end-start+1:
            Globals.sutree[node].append(Globals.sutree[node][io]+Globals.tree[node][io])
            io += 1
        if start!=end:
            Globals.srt(node *2, start, math.trunc((start+end) / float(2)))
            Globals.srt(node *2+1, math.trunc((start+end) / float(2))+1, end)

if __name__ == "__main__":
    main()

# 아니 그냥 이런게 된다로만 봐주세요 실행 안됨