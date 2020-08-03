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
    pass


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
