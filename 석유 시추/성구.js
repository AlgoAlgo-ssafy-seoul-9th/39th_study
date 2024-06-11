function solution(land) {
    let answer = 0;
    
    const [n, m] = [land.length, land[0].length];
    const visited = [];
    for (let i=0; i< n; i++) {
        visited.push(Array(m).fill(0));
    }
    
    const dir = [[0,-1], [0,1], [-1,0], [1,0]];
    
    const bfs = (startI, startJ, index) => {
        const que = {};
        let [front, rear] = [0,0];
        let storage = 1;
        que[rear++] = [startI, startJ];
        while (front !== rear) {
            const [i,j] = que[front++];
            for (let [di, dj] of dir){
                const [ni, nj] = [i+di, j+dj];
                if (0 <= ni && ni < n && 0 <= nj && nj < m && visited[ni][nj] === 0 && land[ni][nj] === 1) {
                    que[rear++] = [ni,nj];
                    visited[ni][nj] = index;
                    storage ++;
                }
            }
        }
        return storage;
    }
    
    let cnt = 1;
    const oils = [0];
    
    
    for (let i=0; i< n; i++){
        for (let j=0; j< m; j++){
            if (visited[i][j] === 0 && land[i][j] === 1) {
                visited[i][j] = cnt
                oils.push(bfs(i,j,cnt++))
            }
        }
    }
    
    
    const v = new Set();
    
    for (let j=0; j<m; j++){
        let oil = 0;
        v.clear();
        for (let i=0; i<n; i++){
            if (!v.has(visited[i][j])){
                v.add(visited[i][j]);
                oil += oils[visited[i][j]];
            }
        }
        answer = Math.max(answer, oil)
    }
    
    return answer;
}