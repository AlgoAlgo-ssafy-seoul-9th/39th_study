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