import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
class MyGridLayout(GridLayout):
    # initializing keywords
    def __init__(self, **kwargs):
        # calling the grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # setting the columns
        self.cols = 2
        # Adding widgets
        self.add_widget(Label(text='Name: '))
        # Adding input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Favorite Pizza: '))
        # Adding input Box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        self.add_widget(Label(text='Favorite color: '))
        # Adding input Box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)

        #create a submit button
        self.submit = Button(text="Submit", font_size=32)
        # Binding button
        self.submit.bind(on_press=self.press)

        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'Hellow {name}, you like {pizza} pizza, and your favorite color is {color}!')
        self.add_widget(Label(text= f'Hellow {name}, you like {pizza} pizza, and your favorite color is {color}!'))

        # clearing the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color`.text = ""
class PolymathApp(App):
    def build(self):
        return MyGridLayout()
        

if __name__ == "__main__":
    PolymathApp().run()