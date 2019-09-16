# 4421 단지 번호 붙이기 문제 풀이
### 1. 선생님 풀이
```python
n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))

def check(i,j):
    return 0<=i< n and 0<= j < n

def BFS(i,j):
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    visited = []
    queue = [(i,j)]
    m[i][j] = 2
    while queue:
        v=queue.pop()
        if v not in visited :
            visited.append(v)
        for k in range(4):
            if check(v[0]+dy[k],v[1]+dx[k]) and m[v[0]+dy[k]][v[1]+dx[k]]== '1' :
                m[v[0]+dy[k]][v[1]+dx[k]]=2
                queue.insert(0,(v[0]+dy[k],v[1]+dx[k]))
    return len(visited)


apt=[]
for i in range(n):
    for j in range(n):
        if m[i][j] =='1':
            apt.append(BFS(i,j))
                                   
print(len(apt))
for i in sorted(apt):
    print(i)
```
  
### 2. 이예찬 풀이
```python
n = int(input())
apart = [['0']*(n+2)]
for i in range(n) :
    apart.append(list('0'+input()+'0'))
apart.append(['0']*(n+2))
result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def BFS(x, y) :
    cnt = 1
    apart[x][y] = '2'
    queue = [(x,y)]
    while queue :
        x, y = queue.pop()
        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if (apart[nx][ny]=='1') :
                apart[nx][ny]='2'
                cnt += 1
                queue.insert(0, (nx, ny))
    return cnt

for i in range(1, n+1) :
    for j in range(1, n+1) :
        if apart[i][j] =='1' :
            result.append(BFS(i, j))
            
print(len(result))

for k in sorted(result) :
    print(k)
```  
