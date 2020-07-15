from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from DataStructureRepresenter.helper import screen_helper
from kivy.core.window import Window

Window.size = (800, 700)


class Stack(Screen):
    pass


class DoublyLinkedList(Screen):
    pass


class Queue(Screen):
    pass


class LinkedList(Screen):
    pass


class DsSelecter(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(Stack(name='stack'))
sm.add_widget(Queue(name='q'))
sm.add_widget(DoublyLinkedList(name='dll'))
sm.add_widget(LinkedList(name='ll'))
sm.add_widget(DsSelecter(name='ds'))


class DataStructureRepresenter(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(screen_helper)
        return screen


app = DataStructureRepresenter()
app.run()
