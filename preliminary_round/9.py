a,b=map(int,input().split())
map=[list(input())for i in range(a)]
move=[]
#sp=[[1,0]]
#lnt=[8]
#move=[[0,0],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8]]
sp=[[0,1],[0,7],[0,13],[0,19],\
    [2,23],[2,18],[2,12],[2,6],\
    [4,0],[4,6],[4,12],[4,18],\
    [6,23],[6,17],[6,11],[6,5],\
    [8,0],[8,6],[8,12],[8,18],\
    [10,23],[10,17],[10,11],[10,5],\
    [12,0],[12,6],[12,12],[12,18],\
    [14,23],[14,17],[14,11],[14,5],\
    [16,0],[16,6],[16,12],[16,18],\
    [18,23],[18,17],[18,11],[18,5],\
    [20,0],[20,6],[20,12],\
    [21,24],\
    [22,17],[22,11],[22,5],\
    [24,1],[24,6],[24,12],[24,22]]
lnt=[4,4,4,3,\
     3,4,4,4,\
     4,4,4,4,\
     4,4,4,4,\
     4,4,4,4,\
     4,4,4,4,\
     4,4,4,4,\
     4,4,4,4,\
     4,4,4,4,\
     4,4,4,4,\
     4,4,4,\
     2,4,4,4,\
     3,4,4,2]
#mx=[5,9,8,7,8,5,9,7,7,9,8,5,9,5,8,\
#    8,5,9,5,8,9,7,7,9,5,8,7,8,9,5,\
#    7,8,9,5,5,7,9,8,9,8,5,7,5,8,7,9,\
#    9,7,8,5,7,5,8,9,8,9,7,5,5,9,8,7,\
#    5,7,9,8,9,8,5,7,5,8,7,9,7,5,9,8,\
#    8,9,5,7,9,7,8,5,7,5,8,9,8,9,7,5]
st=[0]*(sum(lnt)+1)
ch=0
y=0
dy=[-1,0,1,0]
dx=[0,1,0,-1]
idx={}
for i in range(13):
    if ch==0:
        for g in range(25):
            move.append([y,g])
        move.append([y+1,24])
        ch=1
    else:
        for g in range(24,-1,-1):
            move.append([y,g])
        move.append([y+1,0])
        ch=0
    y+=2
asd=[[0 for i in range(b+1)]for g in range(a+1)]
for g in range(a):
    for z in range(b):
        if map[g][z]!="."and map[g][z]!="#":
            for k in range(4):
                nx=z+dx[k]
                ny=g+dy[k]
                if 0<=nx<b and 0<=ny<a:
                    asd[ny][nx]=1
acnt=0
#print(asd)
for ix in range(1,len(move)):
    #print(move[ix])
    if asd[move[ix][0]][move[ix][1]]==1:
        #print(move[ix][0]*b+move[ix][1])
        idx[move[ix][0]*b+move[ix][1]]=acnt
        acnt+=1
#print(idx)
#print(move)
#print(len(move))
ch=0
ans=""
up=len(move)
i=0
chk=0
cnt=-1
last=-1
while i<up:
    if i==0:i+=1;continue
    if last!=i:
        if move[i-1][0]==move[i][0]:
            if move[i-1][1]+1==move[i][1]:
                ans+="R"
            else:
                ans+="L"
        elif move[i-1][0]+1==move[i][0]:
            ans+="D"
        else:
            ans+="U"
    zm=[[0 for i in range(b)]for g in range(a)]
    for g in range(a):
        for z in range(b):
            if map[g][z]!="."and map[g][z]!="#":
                for k in range(4):
                    nx=z+dx[k]
                    ny=g+dy[k]
                    if 0<=nx<b and 0<=ny<a:
                        if map[ny][nx]=="." and zm[ny][nx]==0:
                            if ny==0 and nx==0:continue
                            #print(ny*b+nx,ny,nx,b)
                            fh=idx[ny*b+nx]
                            st[fh]-=1
                            if st[fh]<0:st[fh]=int(map[g][z])-1
                            zm[ny][nx]=1
    #print(sp[ch],move[i],chk,ch)
    #if ch!=0:print(ch)
    if last!=i:print(i);last=i;print("#####")
        #if i==293:
        #    print(move[i])
        
    #print(ch,i)
    #print(chk,ch)
    ggg=0
    #for ii in range(lnt[ch]):
    #    if st[chk+ii]!=ii+1:ggg=1
    #if ggg==0:
    #    for ii in range(lnt[ch]):
    #        print(st[chk+ii],end=" ")
    #    print()
    #    print()
    #if i==293 and cnt<=90:
    #    print(cnt,lnt[ch],ch,chk)
    #    for ii in range(lnt[ch]):
    #        print(st[chk+ii],end=" ")
    #    print()
    #    print()
    if ch<len(sp) and sp[ch]==move[i]:
        #print(sp[ch])
        if cnt==-1:cnt=0
        else:cnt+=1
        #if cnt>=10000:print("#")
        if cnt%2==0 or cnt%2!=0:
            #if cnt>=2500:
            #    print(cnt,lnt[ch],ch,chk)
            #    for ii in range(lnt[ch]):
            #        print(st[chk+ii],end=" ")
            #    print()
            if cnt!=0:
                if move[i-1][0]==move[i][0]:
                    if move[i-1][1]+1==move[i][1]:
                        if cnt%2==0:ans+="R"
                        else:ans+="L"
                        #ans+="LR"
                    else:
                        if cnt%2==0:ans+="L"
                        else:ans+="R"
                        #ans+="RL"
                elif move[i-1][0]+1==move[i][0]:
                    if cnt%2==0:ans+="D"
                    else:ans+="U"
                    #ans+="UD"
                else:
                    if cnt%2==0:ans+="U"
                    else:ans+="D"
                    #ans+="DU"
            hl=1
            for ii in range(lnt[ch]):
                if st[chk+ii]!=ii+1:hl=0
            if hl==1:
                if cnt%2==0:
                    if i==324:
                        print(move[i])
                        for ii in range(lnt[ch]+2):
                            print(st[chk+ii],end=" ")
                        print()
                        print()
                    #print(move[i])
                    #print("###",i,cnt)#;sys.exit()
                    i+=1;chk+=lnt[ch];cnt=-1;ch+=1
                    #print(i,cnt)
                else:
                    print(move[i])
                    print("###",i,cnt)
    else:i+=1
#print(len(ans))
print(ans[:60000])
#print(ans)
#for i in range(10000):
#    print(ans[i],end="")