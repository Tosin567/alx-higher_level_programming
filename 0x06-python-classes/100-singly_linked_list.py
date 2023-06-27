#!/usr/bin/python3



class Node:
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self._data = data

        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError('next_node must be a Node object')
        self._next_node = next_node

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self._next_node = value

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __str__(self):
        current = self._head
        string_list = []
        while current:
            string_list.append(str(current.data))
            current = current.next_node
        string_list = "\n".join(string_list)
        return string_list

    def sorted_insert(self, value):
        new_node = Node(value)

        if self._head is None:
            self._head = new_node
        elif self._head.data > value:
            new_node.next_node = self._head
            self._head = new_node
        else:
            current = self._head

            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
