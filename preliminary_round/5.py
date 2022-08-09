N, M = map(int, input().split()) # 첫 줄에 격자판의 크기를 나타내는 가로 / 세로
fx = open("5.txt", 'a') # 여기서 파일 형식으로 내보내라고 했으니 5.txt 엽니다.
canvas = [] # canvas에 격자판을 채우기 위해 list 형식으로 만듭니다.
color_count = 0 # 색깔의 종류의 색을 새기 위한 color_count를 선언하고 0으로 정합니다.

for i in range(M): # i에 1을 계속 더하며 M-1이 될때까지 반복합니다.
    templist = list(map(int, input().split())) # templist로 격자판의 한줄을 받습니다.
    canvas.append(templist) # canvas에 templist의 리스트를 추가합니다.

for i in range(1, 8): #for i에 1부터 1을 계속 더하며 7까지 반복합니다.
    if any(i in l for l in canvas): # 만약 캔버스에 i값이 포함되어 있다면...
        color_count += 1 #color count에 1을 더합니다.
    else: # 아니라면...
        pass # 건너 뜁니다.

fx.write(f"{str(color_count)}\n") # 5.txt에 color_count를 넣습니다.

# 20,21,23,24는 리스트를 선언하는 코드들 입니다.

f_color = []
s_color = []

f_i = []
s_i = []

for i in range(N): # i에 1을 계속 더하며 N이 될때까지 반복합니다.
    color = 0 # color를 0으로 선언합니다.
    for j in range(M): # j에 1을 계속 더하며 M이 될때까지 반복합니다.
        if canvas[i][j] != 0: # 만약 canvas[i][j]가 0이 아니라면...
            color = canvas[i][j] # color에 can[i][j]를 넣습니다.
            f_color.append(color) # f_color에 color값을 넣습니다.
            f_i.append(i) # f_i에 i값을 넣습니다.
fx.write(f"H {f_i[1]+1} {f_color[1]}\n") # 5.txt에 H f_i[1] f_c[1]을 넣습니다.

for i in range(M): # i에 1을 계속 더하며 M이 될때까지 반복합니다.
    color = 0 # color를 0으로 선언합니다.
    for j in range(N): # j에 1을 계속 더하며 N이 될때까지 반복합니다.
        if canvas[j][i] != 0: # 만약 canvas[i][j]가 0이 아니라면...
            color = canvas[j][i] # color에 canvas[j][i]를 넣습니다.
            s_color.append(color) # s_color에 color값을 넣습니다.
            s_i.append(i) # s_i에 i값을 넣습니다.
fx.write(f"V {s_i[3]+1} {s_color[3]}\n") # 5.txt에 H s_i[3] s_color[3]을 넣습니다.

fx.close() # 5.txt에 이 모든 변경 사항을 저장합니다.