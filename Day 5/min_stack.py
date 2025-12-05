class MinStack:
    def __init__(self):
        self.s = []
        self.min = None
    
    def push(self, x):
        if not self.s:
            self.s.append(x) 
            self.min = x
            return self.s
        
        elif x < self.min:
            self.s.append(2*x - self.min)
            self.min = x
            return self.s

        self.s.append(x)
        return self.s
    
    def pop(self):
        if not self.s:
            return -69
        else:
            popped = self.s.pop()
            if popped < self.min:
                self.min = 2*self.min - popped
        return popped
    
    def peek(self):
        if not self.s:
            return -69
        else:
            if self.s[-1] < self.min:
                return self.min
            else:
                return self.s[-1]
            
    def get_min(self):
        if not self.s:
            return -69
        else:
            return self.min


mystack = MinStack()
print(mystack.push(2), mystack.min)
print(mystack.peek())
print(mystack.get_min())

print(mystack.push(3), mystack.min)
print(mystack.get_min())
print(mystack.peek())

print(mystack.push(1), mystack.min)
print(mystack.get_min())
print(mystack.peek())

print(mystack.push(0), mystack.min)
print(mystack.get_min())
print(mystack.peek())

print("-----------------------------------------------")
print("-----------------------------------------------")

print(mystack.pop(), mystack.min)
print(mystack.pop(), mystack.min)
print(mystack.pop(), mystack.min)


print("-----------------------------------------------")
print("-----------------------------------------------")


    
"""
push, pop, peek, getMin
"""