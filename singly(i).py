class _Node:

    def __init__(self, element, next=None):
        self.element = element
        self.next = next

first = _Node(1)
print(first.element)

