import kivy
from kivy.app import App
from kivy.uix.label import Label

class PolymathApp(App):
    screen = Screen()
    def build(self):
        return Label(text="Hello world", font_size = 60)
        btn_flat = MDFlatButton(text='hello world')

if __name__ == "__main__":
    PolymathApp().run()