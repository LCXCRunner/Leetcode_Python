import sys
# import numpy as np
# import pandas as pd
# from sklearn import ...
class Stack:
    def __init__(self):
        self.elements : list = []
        
    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack empty")
        else:
            return self.elements.pop() # python lists already can act like a stack. Just coding it as intended though. 
        
    def push(self, element):
        return self.elements.append(element)
        
    def isEmpty(self):
        return len(self.elements) == 0
    
    def lenth(self):
        return len(self.elements)
    
    
for line in sys.stdin:
    # setup and create our stack object
    result : list = []
    splitLine = line.split()
    stack : Stack = Stack()
    
    for char in splitLine:
        stack.push(int(char))
    
    # alternate pop+print
    while not stack.isEmpty():
        if stack.lenth() % 2 == 0:
            result.append(stack.pop())
        else:
            stack.pop()
            
    # print it out like the test wants
    strResult = " ".join(str(num) for num in result)
    print(strResult)