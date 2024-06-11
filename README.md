# 39th_study

알고리즘 스터디 39주차

<br/>

# 이번주 스터디 문제

<details markdown="1" open>
<summary>접기/펼치기</summary>

<br/>

## [멍멍이 쓰다듬기](https://www.acmicpc.net/problem/1669)

### [민웅](./멍멍이%20쓰다듬기/민웅.py)

```py

```

### [상미](./멍멍이%20쓰다듬기/상미.py)

```py

```

### [성구](./멍멍이%20쓰다듬기/성구.py)

```py
```

### [영준](./멍멍이%20쓰다듬기/영준.py)

```py
```

<br/>

## [고대 문명 유적 탐사](https://www.codetree.ai/training-field/frequent-problems/problems/ancient-ruin-exploration/description?page=1&pageSize=20)

### [민웅](./고대%20문명%20유적%20탐사/민웅.py)

```py
```

### [상미](./고대%20문명%20유적%20탐사/상미.py)

```py
```

### [성구](./고대%20문명%20유적%20탐사/성구.py)

```py

```

### [영준](./고대%20문명%20유적%20탐사/영준.py)

```py
```

<br/>

## [레이저 통신](https://www.acmicpc.net/problem/6087)

### [민웅](./레이저%20통신/민웅.py)

```py
```

### [상미](./레이저%20통신/상미.py)

```py

```

### [성구](./레이저%20통신/성구.py)

```py
```

### [영준](./레이저%20통신/영준.py)

```py

```

<br/>

</details>

<br/><br/>

# 지난주 스터디 문제

<details markdown="1">
<summary>접기/펼치기</summary>

<br/>

## [석유 시추](https://school.programmers.co.kr/learn/courses/30/lessons/250136)

### [민웅](./석유%20시추/민웅.py)

```py
from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def solution(land):
    answer = 0
    
    h = len(land)
    w = len(land[0])
    
    visited = [[0]*w for _ in range(h)]
    group = [[0]*w for _ in range(h)]
    
    g_idx = 1
    for i in range(h):
        for j in range(w):
            if land[i][j] and not visited[i][j]:
                q = deque()
                tmp = []
                cnt = 0
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    tmp.append((x, y))
                    cnt += 1
                    
                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]
                        
                        if 0 <= nx <= h-1 and 0 <= ny <= w-1:
                            if land[nx][ny] and not visited[nx][ny]:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                for t in tmp:
                    x, y = t
                    group[x][y] = g_idx
                    visited[x][y] = cnt
                g_idx += 1
    
    
    
    for k in range(w):
        tmp_ans = 0
        g_check = set()
        for l in range(h):
            if group[l][k] and group[l][k] not in g_check:
                g_check.add(group[l][k])
                tmp_ans += visited[l][k]
        if tmp_ans > answer:
            answer = tmp_ans
    # print("V =", visited)
    # print("G =", group)
    return answer
```

### [상미](./석유%20시추/상미.py)

```py

```

### [성구](./석유%20시추/성구.py)

```py
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
```

### [영준](./석유%20시추/영준.py)

```py

```

 

</details>

<br/><br/>

# 알고리즘 설명

<details markdown="1">
<summary>접기/펼치기</summary>

</details>
