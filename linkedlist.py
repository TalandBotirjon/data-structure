"""
Linked List Objects.
"""


class Node:
    """Tugun object."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Linked List Object."""

    def __init__(self):
        self.head = None

    def printlist(self):
        """List ma'lumotlarini ekranga chiqarish."""
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def push(self, new_data):
        """List boshiga element qo'shish."""
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertafter(self, prev_node, new_data):
        """Listning istalgan joyiga element qo'shish."""
        if prev_node is Node:
            print('Tugun mavjud emas.')
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        """List oxiriga element qo'shish."""
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete(self, key):
        """Listdan qiymat o'chirish."""
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp.next = None
            return
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

