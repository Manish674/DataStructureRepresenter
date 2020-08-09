import kivy
import kivymd
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


class LinkedList(Screen):
    def __init__(self, **kwargs):
        super(LinkedList, self).__init__(**kwargs)
        self.head = None

    def printLL(self):
        current = self.head
        store = []
        while(current):
            store.append(current.data)
            # print(current.data)
            current = current.next
        return store

    def insert_at_begining(self, data):
        node = Node(self.ll_textfield.text, self.head)
        self.head = node
        self.ll_textfield.text = ''
        self.ll_label.text =  str(self.printLL())

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(self.ll_textfield.text)
            self.ll_textfield.text = ''
            self.ll_label.text =  str(self.printLL())

        self.ll_value_holder = []

    def insert_head(self):
        if self.ll_textfield.text is '':

            return

        self.ll_value_holder.insert(0, str(self.ll_textfield.text) + '-->')
        self.ll_label.text = str(self.ll_value_holder)


        itr.next = Node(self.ll_textfield.text)
        self.ll_textfield.text = ''
        self.ll_label.text =  str(self.printLL())

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove(self, data):
        return
        #TODO


    def insert_after_head(self):
        if self.ll_value_holder is '':
            self.ll_label.text = 'List is empty'
            return

        self.ll_value_holder.append(self.ll_textfield.text + '-->')
        self.ll_label.text = str(self.ll_value_holder)



sm = ScreenManager()
sm.add_widget(Dselecter(name='dss'))
sm.add_widget(Stack(name='stack'))
sm.add_widget(Queue(name='queue'))
sm.add_widget(LinkedList(name='ll'))


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        return


DemoApp().run()


# data, next
# (1, 2)->(2, 3)->(3, 4)->(4, none)
