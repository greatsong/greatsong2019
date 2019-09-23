```python

#0. 맵 만들기
m = ['S......#',
     '...###..',
     '######..',
     '........',
     'G...####']
h = 5
w = 8
Gy = 4
Gx = 0
Sy = 0
Sx = 0

#1. 랜덤 맵 생성 코드
import random
Sy, Sx, Gy, Gx = 0, 0, 0, 0

def createMap(h,w) :
    global Gy, Gx
    tile = '#...'
    m = []
    for i in range(h) :
        line = []
        for j in range(w) :
            line.append(random.choice(tile))
        m.append(line)
    m[Sy][Sx] = 'S'
    Gy = random.randint(1,h-1)
    Gx = random.randint(1,w-1)
    m[Gy][Gx] ='G'
    return m

h = 10
w = 10
m = createMap(h,w)

for i in range(h) :
    print(''.join(m[i]))
    
#2. 알고리즘 : visited 맵 만들기
#visited = [[0] * w for j in range(h)]
visited =[]
for i in range(h) :
    temp = []
    for j in range(w) :
        temp.append(0)
    visited.append(temp)
print(visited)

#3. 준비 작업
def check(i,j) :
    return 0 <= i < h and 0 <= j < w
dx = [0,0,1,-1]
dy = [1,-1,0,0]

#4. 알고리즘 : bfs 함수 만들기
def bfs(m) :
    queue = [(Sy,Sx)]
    while queue :
        v = queue.pop()
        for k in range(4) :
            di = v[0] + dx[k]
            dj = v[1] + dy[k]
            if check(di,dj) and m[di][dj] in '.G'\
            and visited[di][dj] == 0 :
                queue.insert(0, (di,dj))
                visited[di][dj] = visited[v[0]][v[1]] + 1
                if m[di][dj] == 'G' :
                    visited[di][dj] = 'G'
                    visited[Sy][Sx] = 'S'
                    return visited[v[0]][v[1]] + 1
    return -1
                
print(bfs(m))

# 4. 출력 코드
for i in range(h):
    for j in range(w) :
         print(visited[i][j], end = ' ')
    print()
```
