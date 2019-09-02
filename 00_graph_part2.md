[[온라인 교재 - 7장 Graph 구현](https://runestone.academy/runestone/books/published/pythonds/Graphs/Implementation.html)]  

### 1. 정점(Vertex) 클래스 정의
```python
class Vertex:
    def __init__(self,key):
        self.id = key # 정점의 식별자(id)
        self.connectedTo = {} # 정점과 연결된 정점들(키는 정점 id, 값은 가중치)

    def addNeighbor(self,nbr,weight=0): # 정점에 이웃 정점 연결
        self.connectedTo[nbr] = weight  

    def __str__(self):  # 정점과 연결된 정점들 문자열로 리턴
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):  # 정점과 연결된 정점들 리턴
        return self.connectedTo.keys()

    def getId(self): # 정점 id 리턴
        return self.id

    def getWeight(self,nbr): # 특정 정점과의 가중치 리턴
        return self.connectedTo[nbr]
```

### 2. 그래프(Graph) 클래스 정의
```python
class Graph:
    def __init__(self):
        self.vertList = {}  # 정점들의 리스트(키는 정점 id, 값은 정점 오브젝트)
        self.numVertices = 0 # 정점 갯수

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1 # 정점 갯수 + 1
        newVertex = Vertex(key) # 정점 오브젝트 생성
        self.vertList[key] = newVertex # 정점 리스트에 추가
        return newVertex # 생성된 정점 오브젝트 리턴

    def getVertex(self,n):
        if n in self.vertList: # n(id)에 해당하는 정점 오브젝트 리턴
            return self.vertList[n]
        else: # 없는 id일 경우 None을 리턴
            return None

    def __contains__(self,n):
        return n in self.vertList # n(id) 정점이 그래프에 포함되어있는지 여부 리턴

    def addEdge(self,f,t,cost=0): # 정점 f에서 정점 t로 향하는 가중치가 cost인 간선 추가
        if f not in self.vertList: # f 정점이 없을 경우 추가
            nv = self.addVertex(f)
        if t not in self.vertList: # t 정점이 없을 경우 추가
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost) # 간선 추가

    def getVertices(self): # 그래프에 포함된 정점들 리턴
        return self.vertList.keys()

    def __iter__(self): # 그래프에 포함된 오브젝트들 반복가능한 객체로 리턴
        return iter(self.vertList.values())
```
