from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager


class Dselecter(Screen):
    pass


class Stack(Screen):
    def __init__(self, **kwargs):
        super(Stack, self).__init__(**kwargs)
        self.var_holder = []

    def append_stack(self):
        self.var_holder.append(self.textfield.text)
        self.label.text = str(self.var_holder)
        self.textfield.text = ''

    def pop_stack(self):
        self.var_holder.pop()
        self.label.text = str(self.var_holder)
        self.textfield.text = ''


class Queue(Screen):
    def __init__(self, **kwargs):
        super(Queue, self).__init__(**kwargs)
        self.var_holder1 = []

    def append_queue(self):
        self.var_holder1.append(self.q_textfield.text)
        self.q_label.text = str(self.var_holder1)
        self.q_textfield.text = ''

    def pop_queue(self):
        self.var_holder1.pop(0)
        self.q_label.text = str(self.var_holder1)
        self.q_textfield.text = ''


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(Screen):
    def __init__(self, **kwargs):
        super(LinkedList, self).__init__(**kwargs)
        self.head = None

    def printLL(self):
        current = self.head
        # to store values in one container
        store = []
        while current:
            store.append(f'({current.data} , {str(current.next)}) -->')
            current = current.next
        return store

    def insert_at_begining(self, data):
        node = Node(self.ll_textfield.text, self.head)
        self.head = node
        self.ll_textfield.text = ''
        self.ll_label.text = str(self.printLL())

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(self.ll_textfield.text)
            self.ll_textfield.text = ''
            self.ll_label.text = str(self.printLL())
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(self.ll_textfield.text)
        self.ll_textfield.text = ''
        self.ll_label.text = str(self.printLL())

    def remove(self, index):
        index = int(self.ll_textfield.text)
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        self.ll_label.text = str(self.show_linkedlist())

    def show_linkedlist(self):
        self.ll_label.text = str(self.printLL())

sm = ScreenManager()
sm.add_widget(Dselecter(name='dss'))
sm.add_widget(Stack(name='stack'))
sm.add_widget(Queue(name='queue'))
sm.add_widget(LinkedList(name='ll'))


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        return


DemoApp().run()

# (1, 2)->(2, 3)->(3, 4)->(4, none)
# data, next
