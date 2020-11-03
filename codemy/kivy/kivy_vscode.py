# from kivy.app import App
# from kivy.uix.widget import Widget

# class PongGame(Widget):
#     pass
 
# class PongApp(App):
#     def build(self):
#         return PongGame()

# PongApp().run()

from kivy.app import App
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel, MDIcon

class Polymath(MDApp):
    # def build(self):
    #     return Label(text='Hello world', size_hint=(1, 0.5))
    def build(self):
        # return Label(text="Hello world", font_size = 60)
        screen = Screen()
        btn_flat = MDFlatButton(text='hello world')
        screen.add_widget(btn_flat)
        label = MDLabel(text='Hello World', halign='center', 
        theme_text_color='Custom', text_color= (236/255.0, 98/255.0, 81/255.0, 20),
        font_style='Caption') # colors available secondary, primary, error, hint

        icon_label = MDIcon(icon='library-video', halign='center')
        return icon_label

Polymath().run()