### 1. 그래프(Graph)란?  
- 여러 노드``(node)``또는 정점``(vertex)``들이 간선``(edge)``으로 연결된 네트워크를 의미함  
- 그래프는 노드와 간선의 집합으로 정의됨.  
<b><i>``G =(V,E)``</i></b>
![그래프 이미지](https://runestone.academy/runestone/books/published/pythonds/_images/digraph.png)

### 2. 그래프의 종류
- 유향``(directed)`` 그래프 vs 무향``(undirected)`` 그래프
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
