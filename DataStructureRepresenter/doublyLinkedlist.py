dll_code = '''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else :
            new_node = Node(data)
            new_node.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def print_dll(self):
        cur = self.head
        while cur:
            print(str(cur.data))
            cur = cur.next

dll = DoublyLinkedList()
dll.append(3)
dll.append(13)
dll.prepend(45)
dll.append(4)
dll.append(78)
dll.print_dll()'''