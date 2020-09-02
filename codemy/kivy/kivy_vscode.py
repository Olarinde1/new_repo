# from kivy.app import App
# from kivy.uix.widget import Widget

# class PongGame(Widget):
#     pass
 
# class PongApp(App):
#     def build(self):
#         return PongGame()

# PongApp().run()

from kivy.app import App
from kivy.uix.label import Label

class Polymath(App):
    def build(self):
        return Label(text='Hello world', size_hint=(1, 0.5))

Polymath().run()