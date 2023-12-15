> the following code block is made with an intent to answer the questions on Linked List and CRUD applications on them


```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # to add elements at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert(self, data, position): # to add elements at some index
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                if current is None:
                    raise IndexError("Position out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def delete(self, position): # to delete elements at some index
        if self.head is None:
            raise IndexError("List is empty")
        if position == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(position - 1):
                if current.next is None:
                    raise IndexError("Position out of range")
                current = current.next
            if current.next is None:
                raise IndexError("Position out of range")
            current.next = current.next.next

    def update(self, data, position):  # to update a certain element
        if self.head is None:
            raise IndexError("List is empty")
        current = self.head
        for _ in range(position):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        if current is None:
            raise IndexError("Position out of range")
        current.data = data

    def display(self): # the method which shows us result
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
```
> the code block below demonstrates implementation of queues in linked list.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return item

    def peek(self):
        if not self.is_empty():
            return self.front.data

    def is_empty(self):
        return self.front is None

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

```

> the following one demonstrates Stack Implementation using Linked List:

```python 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            item = self.top.data
            self.top = self.top.next
            return item

    def peek(self):
        if not self.is_empty():
            return self.top.data

    def is_empty(self):
        return self.top is None

    def size(self):
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return count
```

