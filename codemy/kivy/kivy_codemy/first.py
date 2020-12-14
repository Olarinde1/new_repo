from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('builder.kv')

class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    # initializing keywords
    # def __init__(self, **kwargs):
    #     # calling the grid layout constructor
    #     super(MyGridLayout, self).__init__(**kwargs)
    #     # setting the columns
    #     self.cols = 1
    #     self.row_force_default = True
    #     self.row_default_height = 120
    #     self.col_force_default = True
    #     self.col_default_width = 100
    #     # Creating a second grid layout
    #     self.top_grid = GridLayout(row_force_default=True,
    #                                row_default_height=40,
    #                                col_force_default=True,
    #                                col_default_width=100)
    #     self.top_grid.cols = 2
    #
    #     # Adding widgets
    #     self.top_grid.add_widget(Label(text='Name: '))
    #     # Adding input Box
    #     self.name = TextInput(multiline=True,
    #                           font_size=32,
    #                           size_hint_y=None,
    #                           height=50,
    #                           size_hint_x=None,
    #                           width=200
    #                           )
    #
    #     self.top_grid.add_widget(self.name)
    #
    #     self.top_grid.add_widget(Label(text='Favorite Pizza: '))
    # # Adding input Box
    #     self.pizza = TextInput(multiline=False,
    #                        font_size=32,
    #                        size_hint_y=None,
    #                        height=50,
    #                        size_hint_x=None,
    #                        width=200
    #                        )
    #     self.top_grid.add_widget(self.pizza)
    #
    #     self.top_grid.add_widget(Label(text='Favorite color: '))
    # # Adding input Box
    #     self.color = TextInput(multiline=False,
    #                        font_size=32,
    #                        size_hint_y=None,
    #                        height=50,
    #                        size_hint_x=None,
    #                        width=200
    #                        )
    #     self.top_grid.add_widget(self.color)
    # # Adding the new top_grid to the app
    #     self.add_widget(self.top_grid)
    # # create a submit button
    #     self.submit = Button(text="Submit",
    #                      font_size=32,
    #                      size_hint_y=None,
    #                      height=50,
    #                      size_hint_x=None,
    #                      width=150)
    # # Binding button
    #     self.submit.bind(on_press=self.press)
    #
    #     self.add_widget(self.submit)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f'Hellow {name}, you like {pizza} pizza, and your favorite color is {color}!')
        # self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!'))
        print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!')
        # clearing the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class AlliApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == "__main__":
    AlliApp().run()
