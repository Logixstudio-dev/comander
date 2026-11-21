from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.core.window import Window

from tkinter import filedialog as fd

Window.size = (500, 500)
Window.title = "ComanderIDE Editor"

class Editor(BoxLayout):

    def start_stop(self):
        code = self.ids.code_input.text.strip()
        return code

    def open_file():
        pass

    def save_file():
        pass

class EditorApp(App):

    def build(self):
        return Editor()



if __name__ == "__main__":
    app = EditorApp()
    app.run()

