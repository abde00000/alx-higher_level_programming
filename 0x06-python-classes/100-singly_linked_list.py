#!/usr/bin/python3

"""Defines a singly linked list."""


class Node:
    """Represents the class Node."""
    def __init__(self, data, next_node=None):
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Get the data value."""
        return self._data

    @data.setter
    def data(self, value):
        """Set the data value."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self._data = value

    @property
    def next_node(self):
        """Get the next_node value."""
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """set the next_node value."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """Represents the singlyLinked list class."""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.head is None or self.head.data >= new_node.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next_node and\
                    last_node.next_node.data < new_node.data:
                last_node = last_node.next_node
            new_node.next_node = last_node.next_node
            last_node.next_node = new_node

    def __str__(self):
        list_str = ""
        current_node = self.head
        while current_node:
            list_str += str(current_node.data)
            if current_node.next_node:
                list_str += "\n"
            current_node = current_node.next_node
        return list_str
