class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message

class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.next = succeeding
        self.prev = previous


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __len__(self):
        length = 0
        current_node = self.head

        while current_node is not None:
            current_node = current_node.next
            length += 1

        return length

    def push(self, value):
        if len(self) == 0:
            self.head = Node(value)
        else:
            current_node = self.head

            while current_node is not None:
                current_node.next.prev = current_node
                current_node = current_node.next

            new_node = Node(value, previous=current_node)
            current_node.next = new_node

    def pop(self):
        if len(self) == 0:
            raise IndexError('List is empty.')


    # Removes element from the beginning of list.
    def shift(self):
        if len(self) == 0:
            raise IndexError('Value not found')

    # Adds element at start of list.
    def unshift(self, values):
        pass

    # If value appears more than once, only the first occurrence should be removed.
    def delete(self, value):
        if len(self) == 0:
            raise ValueError('Value not found')