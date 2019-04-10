# Stack 클래스와 함수를 사용한 문제해결방법

class Stack :
    def __init__(self, k=[]) : 
        self.items = k
    def isEmpty(self):
        return self.items == []
    def push(self,item) :
        self.items.append(item)
    def pop(self) :
        return self.items.pop()
    def peek(self) :
        return self.items[-1]
    def size(self) :
        return len(self.items)

s = Stack()
txt = input()
def checker(string) : 
    for i in string : 
        if i == '(' :
            s.push(i)
        else : 
            if s.isEmpty() :
                return False
            else :
                s.pop()
    if s.isEmpty() :
        return True
    else :
        return False
    
if checker(txt) :
    print('good')
    
else :
    print('bad')
