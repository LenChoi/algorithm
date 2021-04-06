position = input()
x, y = position[0], int(position[1])
count = 0

change = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

for i in range(len(change)):
    if x == change[i]:
        x = int(i+1)
        print(x)
        

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx > 0 and ny > 0 and nx < 9 and ny < 9:
        count += 1

print(count)
