# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:39:39 2017

@author: aidan
"""

class Stack:
    
    def __init__(self):
        self.stacks = []
        
    def top(self):
        return self.stacks[len(self.stacks)]
    
    def pop(self):
        return self.stacks.pop()
    
    def push(self, num):
        self.stacks.append(num)
        
    def isEmpty(self):
        if(self.stacks == []):
            return True
        else:
            return False
    def __str__(self):
        return str(self.stacks)
            



stack = Stack()  
    
print('isEmpty():', stack.isEmpty())
print('empty:', stack)
stack.push(1)
print('after push(1):', stack)
print('isEmpty():', stack.isEmpty())
stack.push(10)
print('after push(10):', stack)
print('pop():', stack.pop())
print('after pop():', stack)
stack.push(2)
print('after push(2):', stack)
stack.push(3)
print('after push(3):', stack)
stack.push(4)
print('after push(4):', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('pop():', stack.pop())
print('after pop():', stack)
print('isEmpty():', stack.isEmpty())  
