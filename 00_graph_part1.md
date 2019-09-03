[[온라인 교재 - 7장 Graph](https://runestone.academy/runestone/books/published/pythonds/Graphs/Objectives.html)]  
# step 1. 그래프 개념 이해하기
### 1. 그래프(Graph)란?  
- 여러 노드`(node)`또는 정점`(vertex)`들이 간선`(edge)`으로 연결된 네트워크를 의미함  
- 그래프는 노드와 간선의 집합으로 정의됨  
- <b><i>``G =(V,E)``</i></b>

![그래프 이미지](https://runestone.academy/runestone/books/published/pythonds/_images/digraph.png)
> Q1. 우리 주변에 그래프로 모델링할 수 있는 것들에는 어떤 것이 있을까?

### 2. 그래프의 종류
- 방향``(directed)`` 그래프 vs 무방향``(undirected)`` 그래프
- 가중치``(weighted)`` 그래프 vs 무가중치``(unweighted)`` 그래프

> [[관련 링크 : 위키 - 그래프](https://ko.wikipedia.org/wiki/그래프)]  
> [[관련 링크 : 위키 - 그래프_이론](https://ko.wikipedia.org/wiki/그래프_이론)]

### 3. 그래프의 Abstract Data Type  
- `Graph()` creates a new, empty graph.
- `addVertex(vert)` adds an instance of `Vertex` to the graph.
- `addEdge(fromVert, toVert)` Adds a new, directed edge to the graph that connects two vertices.
- `addEdge(fromVert, toVert, weight)` Adds a new, weighted, directed edge to the graph that connects two vertices.
- `getVertex(vertKey)` finds the vertex in the graph named `vertKey`.
- `getVertices()` returns the list of all vertices in the graph.
- `in` returns `True` for a statement of the form `vertex in graph`, if the given vertex is in the graph, `False` otherwise.

### 4. 인접 행렬(An Adjacency Matrix)
- 각각의 행과 열은 그래프의 정점을 나타냄
- 행렬에 저장되는 값은 정점 <i>v</i>에서 정점 <i>w</i>으로 연결된 간선의 가중치를 의미함(가중치가 없을 경우 1로 표기)
- 정점 <i>v</i>가 정점 <i>w</i>와 연결되었을 때 정점 <i>v</i>와 정점 <i>w</i>는 서로 인접(adjacent)함
![인접 행렬 이미지](https://runestone.academy/runestone/books/published/pythonds/_images/adjMat.png)

> Q2. 인접 행렬의 장점은 구현이 간단하다는 점이다. 그렇다면 인접 행렬의 단점은 무엇일까?

### 5. 인접 리스트(An Adjacency List)
- 그래프 오브젝트에 여러 개의 정점 오브젝트가 포함됨
- 각각의 정점 오브젝트에는 오브젝트 id와 인접한 정점의 id와 간선의 가중치가 저장됨(딕셔너리로 구현)
![인접 리스트 이미지](https://runestone.academy/runestone/books/published/pythonds/_images/adjlist.png)
