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
        if len(self) == 1:
            return self.head.value

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

            while current_node.next is not None:
                current_node.next.prev = current_node
                current_node = current_node.next

            new_node = Node(value, previous=current_node)
            current_node.next = new_node

    def pop(self):
        if len(self) == 0:
            raise IndexError('List is empty.')

        if len(self) == 1:
            current_node = self.head
            self.head = None
            return current_node.value

        current_node = self.head
        previous_node = current_node.prev

        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next

        previous_node.next = None

        return current_node.value

    # Removes element from the beginning of list.
    def shift(self):
        if len(self) == 0:
            raise IndexError('List is empty')

        old_head = self.head
        new_head = old_head.next

        self.head = new_head

        return old_head.value

    # Adds element at start of list.
    def unshift(self, value):
        new_head = Node(value, succeeding=self.head)
        self.head = new_head

    # If value appears more than once, only the first occurrence should be removed.
    def delete(self, value):
        if len(self) == 0:
            raise ValueError('Value not found')

        current_node = self.head

        while current_node.value != value and current_node.next is not None:
            current_node = current_node.next

        if current_node.value != value:
            raise ValueError('Value not found')

        prev_node = current_node.prev
        next_node = current_node.next

        if prev_node is None:
            self.head = next_node
        else:
            prev_node.next = next_node
