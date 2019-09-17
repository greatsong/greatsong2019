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

# 4. 출력 코드
for i in range(h):
    for j in range(w) :
         print(visited[i][j], end = ' ')
    print()
```
