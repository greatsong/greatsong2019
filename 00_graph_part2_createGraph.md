# step 2. 그래프 이해하기
### ``[가중치가 없는 무방향 그래프]``
### 1. 다음 그래프는 딕셔너리로 표현하면 다음과 같습니다.
![그래프 이미지](http://cfile223.uf.daum.net/image/2610974C539D5C81021EB7)  
```python
{1: [2,3], 2: [1,4,5], 3: [1,4,6], 4: [2,3,5,7], 5: [2,4,7], 6: [3,7], 7: [4,5,6]}
```


### 2. 다음 코드를 실행한 결과를 화이트보드에 그래프로 그려보세요.
![그래프 이미지](https://upload.wikimedia.org/wikipedia/commons/thumb/3/33/Breadth-first-tree.svg/1280px-Breadth-first-tree.svg.png)

### ``[가중치가 없는 방향 그래프]``
### 3. 다음 코드의 목적과 각 라인의 의미를 옆 친구에게 설명해주세요.

```python
def createGraph(n) :
    import random
    graph = {}
    for i in range(n) : 
        size = random.randint(1, n // 2 - 1)
        num = list(range(n))
        random.shuffle(num)
        num.remove(i) 
        graph[i] =  sorted(num[:size])
    return graph
```

### 4. 다음 코드를 실행한 결과를 화이트보드에 그래프로 그려보세요.
1. {0: [1], 1: [4], 2: [0], 3: [2], 4: [2]}
2. {0: [4], 1: [0, 4, 5], 2: [4], 3: [0, 1, 4], 4: [0, 1, 5], 5: [2, 4]}
3. {0: [2, 3, 5], 1: [2, 5, 7], 2: [3], 3: [0, 7], 4: [0], 5: [4, 6], 6: [0, 2, 7], 7: [1, 2]}