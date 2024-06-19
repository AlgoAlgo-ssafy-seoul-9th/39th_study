# 6087 레이저 통신
import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
geo = tuple(input().strip() for _ in range(H))

point = []
for i in range(H):
    for j in range(W):
        if geo[i][j] == 'C':
            point.append((i,j))

def bfs(start, end):
    que = deque()
    visited = [[[10000,10000,10000,10000] for _ in range(W)]  for _ in range(H)]
    direction = [(0,1), (0,-1), (1,0), (-1,0)]

    for d in range(4):
        visited[start[0]][start[1]][d] = 0
        di, dj = direction[d]
        ni,nj = di+start[0], dj+start[1]
        if 0 <= ni < H and 0 <= nj < W and geo[ni][nj] != "*":
            visited[ni][nj][d] = 0
            que.append((ni,nj))

    while que:
        i, j= que.popleft()
        if (i,j) == end:
            continue
        
        for k in range(4):      # 방향순회
            di,dj = direction[k]
            ni, nj = di+i, dj+j

            if 0 > ni or 0 > nj or W <= nj or H <= ni or geo[ni][nj]=="*":
                continue
        
            min_value = visited[ni][nj][k]
            for d in range(4):      # visited[i][j] 순회
                if k != d:
                    min_value = min(min_value, visited[i][j][d]+1)
                else:
                    min_value = min(min_value, visited[i][j][d])
            
            if min_value < visited[ni][nj][k]:
                visited[ni][nj][k] = min_value
                que.append((ni,nj))

    # [print(visited[a]) for a in range(H)]
    return min(visited[end[0]][end[1]])

print(bfs(*point))