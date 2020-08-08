class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('linked list is empty')
            return

        itr = self.head
        ll_str = ''
        while itr:
            ll_str += str(itr.data) + '-->'
            itr = itr.next
        print(ll_str)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr  = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next



# ll = LinkedList()

# no_of_values = int(input('how many values you want to enter'))
# for i in range(int(no_of_values)):
#     user_input = input('Enter your values')
#     place = int(input('Where you want to enter your value \n1) head\n2) before head\n3) at the end'))
#
#     if place == 1:
#         ll.insert_at_begining(user_input)
#
#     elif place ==2:
#         ll.insert_at_begining(user_input)
#
#     elif place ==3:
#         ll.insert_at_end(user_input)

# ll.print()