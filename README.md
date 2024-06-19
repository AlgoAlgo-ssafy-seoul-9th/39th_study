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
# 1669_멍멍이 쓰다듬기_petting a puppy
import sys
input = sys.stdin.readline

monkey, puppy = map(int, input().split())

goal = puppy - monkey

if goal == 0:
    print(0)
else:
    day = int(goal ** (1/2))
    # print(goal ** (1/2), day)
    if day**2 == goal:
        ans = day*2 - 1
    elif day**2 < goal <= day**2 + day:
        ans = day*2
    else:
        ans = day*2 + 1

    print(ans)

# 1 2 1 - 4
# 1 2 1 1 - 5
# 1 2 2 1 - 6
# 1 2 2 1 1 - 7
# 1 2 2 2 1 - 8
# 1 2 3 2 1 - 9
# 1 1 2 3 2 1 - 10
# 1 2 2 3 2 1 - 11
# 1 2 3 3 2 1 - 12
# 1 2 3 3 2 1 1 - 13
# 1 2 2 3 3 2 1 - 14
# 1 2 3 3 3 2 1 - 15
# 1 2 3 4 3 2 1 - 16
```

### [상미](./멍멍이%20쓰다듬기/상미.py)

```py
import sys
input = sys.stdin.readline

monkey, dog = map(int, input().split())
d = dog - monkey
if d == 0:
    print(0)
elif d == 1:
    print(1)
elif d == 2:
    print(2)
else:
    for i in range(2, 2**16):
        if (i-1)**2 < d <= ((i-1)**2 + i**2)//2:
            print(2*i-2)
            break
        elif ((i-1)**2 + i**2)//2 < d <= i**2:
            print(2*i-1)
            break
'''
1: 1            => 1일
2: 1 1          => 2일
3: 1 1 1
4: 1 2 1        => 3일 (2*2-1)
5: 1 2 1 1
6: 1 2 2 1      => 4일 ()
7: 1 2 2 1 1
8: 1 2 2 2 1
9: 1 2 3 2 1    => 5일 (2*3-1)
10: 1 2 3 2 1 1
11: 1 2 3 2 2 1
12: 1 2 3 3 2 1
13:
14:
15:
16: 1 2 3 4 3 2 1   => 7일 (2*4-1)

20:

25:
제곱 수 기준으로 나눠짐

'''
```

### [성구](./멍멍이%20쓰다듬기/성구.py)

```py
# 1669 멍멍이 쓰다듬기
import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

target= Y-X

if target in (0, 1, 2, 3):
    print(target)
else:
    day = int(target ** (1/2) )
    if target == day ** 2:
        print(day+day-1)
    elif day * (day+1) >= target :
        print(day+day)
    else:
        print(day+day+1)

```

### [영준](./멍멍이%20쓰다듬기/영준.py)

```py

```

<br/>

## [고대 문명 유적 탐사](https://www.codetree.ai/training-field/frequent-problems/problems/ancient-ruin-exploration/description?page=1&pageSize=20)

### [민웅](./고대%20문명%20유적%20탐사/민웅.py)

```py
import sys
from collections import deque
dxy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
input = sys.stdin.readline


def rotate(lst, x, y):
    tmp = [[lst[i][j] for j in range(5)] for i in range(5)]

    for i in range(3):
        for j in range(3):
            tmp[x-1+i][y-1+j] = lst[x-1+2-j][y-1+i]

    return tmp


def boom_check(lst):
    visited = [[0] * 5 for _ in range(5)]
    cnt = 0
    for i in range(5):
        for j in range(5):
            if not visited[i][j] and lst[i][j] != -1:
                q = deque()
                num = lst[i][j]
                q.append([i, j])
                visited[i][j] = 1
                group = []

                tmp_cnt = 0
                while q:
                    x, y = q.popleft()
                    tmp_cnt += 1
                    group.append([x, y])

                    for d in dxy:
                        nx = x + d[0]
                        ny = y + d[1]

                        if 0 <= nx <= 4 and 0 <= ny <= 4:
                            if lst[nx][ny] == num and not visited[nx][ny]:
                                q.append([nx, ny])
                                visited[nx][ny] = 1
                if tmp_cnt > 2:
                    cnt += tmp_cnt
                    for g in group:
                        lst[g[0]][g[1]] = -1
    return cnt, lst


def phase1(lst):
    ans = 0
    # 행, 열, 회전 수(90, 180, 270)
    ans_rct = [0, 0, 0]
    ans_lst = []
    for r in range(1, 4):
        for c in range(1, 4):
            tmp = [[lst[i][j] for j in range(5)] for i in range(5)]
            for t in range(1, 4):
                tmp = rotate(tmp, r, c)
                b_tmp = [[tmp[i][j] for j in range(5)] for i in range(5)]
                cnt, l = boom_check(b_tmp)

                if cnt > ans:
                    ans = cnt
                    ans_rct = [r, c, 90 * t]
                    ans_lst = l
                elif cnt == ans:
                    if 90*t < ans_rct[2]:
                        ans_rct = [r, c, 90 * t]
                        ans_lst = l
                    elif 90*t == ans_rct[2]:
                        if c < ans_rct[1]:
                            ans_rct = [r, c, 90 * t]
                            ans_lst = l
                        elif c == ans_rct[1]:
                            if r < ans_rct[0]:
                                ans_rct = [r, c, 90 * t]
                                ans_lst = l

    return ans, ans_lst


def phase2(lst, r):
    if not r:
        return lst

    for j in range(5):
        for i in range(4, -1, -1):
            if lst[i][j] == -1:
                if r:
                    lst[i][j] = r.popleft()
                else:
                    break
        if not r:
            break

    return lst


K, M = map(int, input().split())

relic = [list(map(int, input().split())) for _ in range(5)]
remain = deque(map(int, input().split()))

ans_lst = []
ans = 0

while K:
    c, relic = phase1(relic)
    if not c:
        break
    ans += c

    while True:
        relic = phase2(relic, remain)
        c, relic = boom_check(relic)
        if not c:
            break
        ans += c

    K -= 1
    ans_lst.append(ans)
    ans = 0
print(*ans_lst)
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

```

### [상미](./레이저%20통신/상미.py)

```py

```

### [성구](./레이저%20통신/성구.py)

```py
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
import sys
sys.setrecursionlimit(10**6)

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])

    def oil(i, j, amt):
        if j-1 >= 0 and land[i][j-1] and not visited[i][j-1]:
            visited[i][j-1] = 1
            amt = oil(i, j-1, amt +1)

        if i+1 < n and land[i+1][j] and not visited[i+1][j]:
            visited[i+1][j] = 1
            amt = oil(i+1, j, amt +1)

        if j+1 < m and land[i][j+1] and not visited[i][j+1]:
            visited[i][j+1] = 1
            amt = oil(i, j+1, amt +1)

        if i-1 >= 0 and land[i-1][j] and not visited[i-1][j]:
            visited[i-1][j] = 1
            amt = oil(i-1, j, amt +1)

        return amt

    for j in range(m):
        visited = [[0]*m for _ in range(n)]
        amt = 0
        for i in range(n):
            if land[i][j] and not visited[i][j]:
                visited[i][j] = 1
                amt += 1
                amt = oil(i, j, amt)
                # print(amt)
                # print(visited)
                answer = max(amt, answer)

    return answer
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
