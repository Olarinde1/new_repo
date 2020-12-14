from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Design our .kv design file
Builder.load_file('calc.kv')
# setting the app size
Window.size = (500, 600)


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        # creating a variable for whats in the textbox already
        prior = self.ids.calc_input.text
        # Testing for Error
        if 'Error' in prior:
            prior = " "
        # determine if 0 is sitting there already
        if prior == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # creating adding function

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        # joining a plus sign to the number already there
        self.ids.calc_input.text = f'{prior}{sign}'

    # creating a decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "." in prior and '.' not in num_list[-1]:
            prior = f'{prior}.'
            # the output to the text box
            self.ids.calc_input.text = prior
        elif '.' in prior:
            pass
        else:
            # Adding a dot to the end of the number in the text box
            prior = f'{prior}.'
            # the output to the text box
            self.ids.calc_input.text = prior

    # creating a remove function
    def remove(self):
        prior = self.ids.calc_input.text
        remaining_item = prior[:-1]
        prior = remaining_item
        self.ids.calc_input.text = prior

    def plus_minus(self):
        prior = self.ids.calc_input.text
        # test to confirm if a - sign is there already
        if '-' in prior and prior[0] == '-':
            self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # creating the equals function
    def equal(self):
        prior = self.ids.calc_input.text
        # Error handling
        try:
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = 'Error'
        # Addition
        # if "+" in prior:
        #     num_list = prior.split("+")
        #     answer = 0.0
        #     # looping through the list
        #     for number in num_list:
        #         answer += float(number)
        #     # print(answer)
        #     # printing the answer in the text box
        #     self.ids.calc_input.text = str(answer)


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()
