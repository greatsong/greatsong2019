# step 3. 그래프 순회 방법 이해하기
### 1. 다음 그래프를 중복없이 방문하고 그 순서를 화이트보드에 작성해보세요.
![그래프 이미지](http://cfile223.uf.daum.net/image/2610974C539D5C81021EB7)  

### 2. 대표적인 그래프 순회 방법
1. 깊이 우선 탐색(DFS, Depth-First Search)  
2. 너비 우선 탐색(BFS, Breadth-First Search)  
![그래프 이미지](https://t1.daumcdn.net/cfile/tistory/997C3C3E5BD01AF41D)  

### 3. 너비 우선 탐색이란?
> 너비 우선 탐색(Breadth First search, BFS)은 맹목적 탐색방법의 하나로 시작 정점을 방문한 후 시작 정점에 인접한 모든 정점들을 우선 방문하는 방법이다. 더 이상 방문하지 않은 정점이 없을 때까지 방문하지 않은 모든 정점들에 대해서도 너비 우선 탐색을 적용한다. 

### 4. 너비 우선 탐색 알고리즘
1. 방문한 정점 저장할 리스트, 방문 예정 정점 저장할 리스트(큐) 준비
2. 큐에 시작 정점 enqueue
3. 제일 먼저 들어온 정점 v, dequeue
4. 정점 v에 방문한 적이 없다면 방문 리스트에 저장
5. 정점 v와 인접한 정점 n 중 방문한 적이 없는 정점은 큐에 enqueue
6. 큐에 정점이 있는 동안 3 - 5 반복
7. 큐에 정점이 없으면 순회 종료

### 5. 너비 우선 탐색 코드
```python
def BFS(graph, start):
    visited=[]
    queue=[start] # 시작 정점 enqueue
    while queue: # 큐에 정점이 있을 동안 반복
        v = queue.pop() # 제일 먼저 들어온 정점 dequeue(pop)
        if v not in visited: # 만약 정점 v에 방문한 적이 없었다면
            visited.append(v) # 방문한 리스트에 추가
        for n in graph[v]: # v에 연결된 이웃 정점 순회
            if n not in visited: # 이웃 정점 n이 방문하지 않은 정점이라면
                queue.insert(0, n) # enqueue
    return visited
```

### 6. 너비 우선 탐색 실행 코드
```python
n = int(input('그래프 정점의 갯수를 입력하세요 : '))
g = createGraph(n)
print('그래프가 생성되었습니다.\n', g)
start = int(input('시작하려는 정점을 입력하세요 : '))
print(g, start))
```

### 7. 코드를 수정해서 PR을 보내주세요!
