from collections import deque

def solution(land):
    answer = 0
    direction = [(0,-1), (0,1), (-1,0), (1,0)]
    n = len(land)
    m = len(land[0])
    
    def bfs(start_i, start_j, index):
        que = deque([(start_i, start_j)])
        
        storage = 1
        while que:
            i, j = que.popleft()
            
            for di, dj in direction:
                ni,nj = di+i,dj+j
                if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and land[ni][nj]:
                    visited[ni][nj] = index
                    storage += 1        
                    que.append((ni,nj))
        
        return storage 
    
    
    
    visited = [[0] * m for _ in range(n)]
    cnt = 1
    oils = [0]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                visited[i][j]= cnt
                oils.append(bfs(i, j, cnt))
                cnt += 1
    
    print(oils)
    
    # [print(visited[a]) for a in range(n)]
    v = set()
    for j in range(m):
        v.clear()
        oil = 0
        for i in range(n):
            if visited[i][j] not in v:
                v.add(visited[i][j])
                oil += oils[visited[i][j]]
        # print(oil, v)
        answer = max(answer, oil)        
    
    return answer