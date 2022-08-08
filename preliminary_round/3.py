a,b=map(int,input().split())

l=list(map(int,input().split()))
l=[[l[i],i+1]for i in range(a)]
t=list(map(int,input().split()))
t=[[t[i],i+1]for i in range(b)]

l.sort(reverse=True)
t.sort()

st=[[]for i in range(b+1)]
#real code
for i in range(a):
    t.sort(reverse=True)
    for g in range(l[i][0]):
        t[g][0]-=1
        st[t[g][1]].append(l[i][1])
        ''' # Debug
        print(t)
        print(st)
        '''
for i in range(1,b+1):
    zz=len(st[i])
    print(zz,end=" ")
    for g in range(zz):
        print(st[i][g],end=" ")
    print()

'''
# 먼가의 흔적이 남았으니 된겁니다.

dev, workday = map(int, input().split()) # 넥슨에서 일하는 개발자 수를 나타내는 정수(n) / 근무하는 날수를 나타내는 정수 (K)

always_dev_in = list(map(int, input().split())) # 각 개발자가 출근해야 하는 날수
can_week = list(map(int, input().split())) # 매일매일 사무실에서 일할 수 있는 사람 수의 최댓값

""" #debug
print(f"Dev : {dev}")
print(f"Workday : {workday}")
print(f"Dev : {always_dev_in}")
print(f"Can_week : {can_week}")
"""

res = [[0 for col in range(workday)] for row in range(dev)] # res값의 workday를 행으로 dev를 줄로 해서 2차원 리스트를 만듭니다.
#print(f"Res : {res}") # Debug

for i in range(dev): # dev를 i로 넣은 뒤 i 만큼 반복합니다.
    res[0][i] = can_week[i] # res[0][i] 값에 can_week[i]를 넣습니다.

always_dev_in.sort(reverse=True)

for j in range(1, workday-1):
    always_dev_in.sort(reverse=True)
    for i in range(max(can_week)):
        res[j][i] = always_dev_in[0]


# 2중 for문으로 리스트 모두 출력
for i in res: # 리스트의 값을 i로 꺼냅니다.
    for j in i: # 안쪽에 있는 리스트를 하나씩 꺼냅니다.
        if j == 0:
            print(end='')
        else:
            print(j, end=' ') # j를 출력하고 빈칸을 만듭니다.
    print() # 줄바꿈을 위해 빈 print문을 놔둡니다.
'''