# step 4. 깊이 우선 탐색(DFS, Depth-First Search)  
### 1. 대표적인 그래프 순회 방법
1. 깊이 우선 탐색(DFS, Depth-First Search)  
2. 너비 우선 탐색(BFS, Breadth-First Search)  
![그래프 이미지](https://t1.daumcdn.net/cfile/tistory/997C3C3E5BD01AF41D)  

### 2. 깊이 우선 탐색이란?
> 깊이 우선 탐색(depth-first search: DFS)은 맹목적 탐색방법의 하나로 탐색트리의 최근에 첨가된 노드를 선택하고, 이 노드에 적용 가능한 동작자 중 하나를 적용하여 트리에 다음 수준(level)의 한 개의 자식노드를 첨가하며, 첨가된 자식 노드가 목표노드일 때까지 앞의 자식 노드의 첨가 과정을 반복해 가는 방식이다.

### 3. 깊이 우선 탐색 알고리즘
1. 방문한 정점 저장할 리스트 준비
2. graph의 v 정점에서 dfs 탐색 시작
3. 정점 v 방문하기(리스트에 저장)
4. v와 인접한 정점 n 중 방문하지 않은 정점을 만나면 n에서 dfs 탐색 시작(2번으로)
5. 순회가 종료되면 방문한 리스트 리턴

### 4. 깊이 우선 탐색 코드
```python

def dfs(graph, v):
    visited.append(v) # 정점 저장하기
    for n in graph[v] : # 정점의 이웃 정점 순회
        if n not in visited : # 방문하지 않은 정점을 만나면
            dfs(graph, n) # dfs 탐색 시작
    if v == start : # v가 시작 정점일 경우
        return visited # visited 리스트 리턴
```

### 5. 깊이 우선 탐색 실행 코드
```python
visited = [] # 방문한 정점 경로 저장할 리스트
start = 1 # 시작 정점
graph = createGraph(5) # 그래프 만들기
print(graph, start) # 입력 값 확인
print(dfs(graph, start)) # dfs 순회 결과 출력
```

### 6. 코드를 수정해서 PR을 보내주세요!
