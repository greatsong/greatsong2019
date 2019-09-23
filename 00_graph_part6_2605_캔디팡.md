```python
m = []
part = 0
cnt = 0
dx = [1,0,-1,0]
dy = [0,-1,0,1]
for i in range(7) :
    m.append(list(map(int, input().split())))

def check(y,x) :
    return 0 <= y < 7 and 0 <= x < 7

def dfs(y,x,color) :
    global part
    global dx, dy
    if check(y,x) and m[y][x] == color : 
        part += 1
        m[y][x] = -1
        for i in range(4) :
            dfs(y+dy[i], x+dx[i], color)
        
for i in range(7) :
    for j in range(7) :
        if m[i][j] != -1 :
            part = 0
            dfs(i, j, m[i][j])
            if part >= 3 :
                cnt += 1
print(cnt)
```
