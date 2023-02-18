n = int(input())
board = [input().split() for _ in range(n)]

max_count = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            count = 0
            queue = [(i, j)]
            while queue:
                x, y = queue.pop(0)
                if 0 <= x < n and 0 <= y < n and board[x][y] == '.':
                    count += 1
                    board[x][y] = '-'
                    queue.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
            max_count = max(max_count, count)

print(max_count)
