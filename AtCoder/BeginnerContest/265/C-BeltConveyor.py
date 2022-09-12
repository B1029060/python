H, W = map(int, input().split())
grid = [list(input()) for row in range(H)]
x, y = 1, 1
memo = {}
stepBefore = ''
while True:
    tmp = grid[x - 1][y - 1]
    stepBefore = [x, y]
    if tmp == 'U' and x != 1:
        x -= 1
    if tmp == 'D' and x != H:
        x += 1
    if tmp == 'L' and y != 1:
        y -= 1
    if tmp == 'R' and y != W:
        y += 1
    memo.setdefault((x, y), 0)
    memo[(x, y)] += 1
    if stepBefore == [x, y]:
        print(x, y)
        break
    if memo[(x, y)] > 1:
        print(-1)
        break
