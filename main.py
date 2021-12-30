import sys

class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)


items = input('Проверка на cбалансированность скобок:')

stack = Stack()

for item in items:

    if stack.isEmpty() == True:
        stack.push(item)
        if stack.peek() in (')', ']', '}'):
            print('Несбалансированно')
            sys.exit()
        continue

    if stack.peek() == '(':
        if item == ')':
            stack.pop()
            continue
        stack.push(item)
        if stack.peek() in (']', '}'):
            print('Несбалансированно')
            sys.exit()
        continue

    if stack.peek() == '[':
        if item == ']':
            stack.pop()
            continue
        stack.push(item)
        if stack.peek() in (')', '}'):
            print('Несбалансированно')
            sys.exit()
        continue

    if stack.peek() == '{':
        if item == '}':
            stack.pop()
            continue
        stack.push(item)
        if stack.peek() in (')', '}'):
            print('Несбалансированно')
            sys.exit()
        continue


if stack.size() == 0:
    print('Сбалансированно')
else:
    print('Несбалансированно')