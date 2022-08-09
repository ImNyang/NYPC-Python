student = int(input()) # 기말 시험이 끝난 친구들의 수를 입력받습니다. 그리고 받은 값을 student에 넣습니다.
money = list(map(int, input().split())) # 가지고 있는 돈을 입력받습니다. 그리고 받은 값을 money에 넣습니다.

summoney = sum(money) # 모든 친구들의 돈을 summoney에 저장합니다.

moneydi = summoney // student # summoney / student의 몫을 moneydi에 저장합니다.

'''# Debug
print(student)
print(money)
'''

res = 0 # res에 0을 넣습니다.
for i in range(student): # i가 student 값이 될때까지 i에 1을 더하고 아래 코드를 반복한다.
    if money[i] >= moneydi: pass #만약 money[i]가 moneydi이거나 money[i]가 더 크다면 코드를 건너 뜁니다.
    else: # 아니라면...
        res += (moneydi - int(money[i])) # res에 res + (moneydi - money[i])를 저장합니다.

print(res) # res를 출력합니다.