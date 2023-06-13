class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        if self.is_empty():
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next





    def __str__(self):
        current = self.head
        list_to_print = "["
        while current:
            list_to_print += str(current.data) + ","
            current = current.next
        return list_to_print[:-1] + "]"

    def __repr__(self):
        return str(self)





