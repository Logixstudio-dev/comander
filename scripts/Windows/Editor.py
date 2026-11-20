from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

Window.size = (500, 500)
Window.title = "ComanderIDE Editor"

class Editor(BoxLayout):
    pass

class EditorApp(App):

    def build(self):
        return Editor()


if __name__ == "__main__":
    app = EditorApp()
    app.run()