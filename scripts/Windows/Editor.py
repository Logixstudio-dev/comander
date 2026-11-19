from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout



class Editor(BoxLayout):
    pass

class EditorApp(App):

    def build(self):
        return Editor()


if __name__ == "__main__":
    app = EditorApp()
    app.run()