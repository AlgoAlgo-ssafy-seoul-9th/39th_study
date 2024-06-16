# 6087_레이저통신_lasor commu
import sys
from collections import deque
input = sys.stdin.readline

dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]

W, H = map(int, input().split())

field = [list(input().strip()) for _ in range(H)]
ans = float('inf')

start = False
end = False
for i in range(H):
    for j in range(W):
        if field[i][j] == 'C':
            if not start:
                start = [i, j]
                field[i][j] = "S"
            else:
                end = [i, j]
                field[i][j] = "E"
    if end:
        break

# 방향별로 애초에 따로 알 수 있게 변경
visited = [[[10001]*4 for w in range(W)] for _ in range(H)]
# visited = [[10001]*W for _ in range(H)]
# visited[start[0]][start[1]] = 0
q = deque()

for i in range(4):
    nx = start[0] + dxy[i][0]
    ny = start[1] + dxy[i][1]
    if 0 <= nx <= H-1 and 0 <= ny <= W-1 and field[nx][ny] != '*':
        q.append([nx, ny, i, 0])
        # visited[nx][ny] = 0
        visited[nx][ny][i] = 0

while q:
    x, y, d, cnt = q.popleft()

    for i in range(4):
        nx = x + dxy[i][0]
        ny = y + dxy[i][1]
        if 0 <= nx <= H-1 and 0 <= ny <= W-1 and field[nx][ny] != '*':
            tmp_cnt = cnt
            if d != i:
                tmp_cnt += 1

            # 같은경우까지도 체크 해줘야함
            # 했더니 80% 시간초과, 메모리초과
            # if tmp_cnt <= visited[nx][ny]:
            #     visited[nx][ny] = tmp_cnt
            #     q.append([nx, ny, i, tmp_cnt])

            if tmp_cnt < visited[nx][ny][i]:
                visited[nx][ny][i] = tmp_cnt
                q.append([nx, ny, i, tmp_cnt])

# ans = visited[end[0]][end[1]]
ans = min(visited[end[0]][end[1]])
print(ans)
