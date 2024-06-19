import sys
input = sys.stdin.readline

W, H = map(int, input().split())
arr = [list(input().strip()) for _ in range(H)]

C = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'C':
            C.append((i, j))
start = C[0]
end = C[1]

