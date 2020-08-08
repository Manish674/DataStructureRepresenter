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

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
        self.root.ll_textfield.text =  str(self.head.data)
        self.root.ll_textfield.text = self.root.ll_label.text

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)



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
