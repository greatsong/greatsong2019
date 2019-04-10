# 코드업 3127번 문제 풀이

a = input().split()

class Stack :
    def __init__(self) :
        self.items = []
    def push(self, item) :
        self.items.append(item)
    def pop(self):
        return self.items.pop()
         
s = Stack()
for i in a :
    if i in '+' :
        s.push(s.pop()+s.pop())
    elif i in '-' :
        s.push(-(s.pop())+s.pop())
    elif i in '*' :
        s.push(s.pop()*s.pop())
    else :
        s.push(int(i))

print(s.pop())
