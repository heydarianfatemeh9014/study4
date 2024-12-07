from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder

class MyApp(App):
    def build(self):
        return Builder.load_file("main.kv")

if __name__ == "__main__":
    MyApp().run()
