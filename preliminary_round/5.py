
N, M = map(int, input().split())

canvas = []
color_count = 0

for i in range(M):
    templist = list(map(int, input().split()))
    canvas.append(templist)

for i in range(1, 8):
    if any(i in l for l in canvas):
        color_count += 1
    else:
        pass

for i in range(N):
    temp = 0
    for j in range(M):
        if not temp and canvas[i][j]:
            temp = canvas[i][j]
''' # Debug
print(canvas)
'''
print(color_count)
temp = 0
print(f"H {temp} {temp}")
print(f"V {temp} {temp}")
