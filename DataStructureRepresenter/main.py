from kivymd.app import MDApp
from kivy.core.window import Window

Window.size = (500, 600)


class DemoApp(MDApp):
    def build(self):
        return

    def stack(self):
        var_holder = []
        var_holder.append(self.root.ids.textfield.text)
        self.root.ids.label.text = str(var_holder)


DemoApp().run()
