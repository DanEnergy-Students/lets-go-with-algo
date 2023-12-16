'''
In this example, we define a Stack class with the basic operations of push, pop, is_empty, and size. We then define a function reverse_list() that takes a list of names as input.

Inside the reverse_list() function, we create an instance of the Stack class and push each name from the input list onto the stack.

Next, we create an empty list called reversed_names. We pop elements from the stack one by one and append them to reversed_names. 
 Since the stack follows the Last-In-First-Out (LIFO) principle, popping the elements in this manner  reverses the order.

Finally, we return the reversed list of names.

'''


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def reverse_list(names):
    stack = Stack()
    for name in names:
        stack.push(name)

    reversed_names = []
    while not stack.is_empty():
        reversed_names.append(stack.pop())

    return reversed_names


# Example 
name_list = ["Fetih", "Girma", "Einstein", "Adane", "Alazar"]
reversed_list = reverse_list(name_list)
print(reversed_list)