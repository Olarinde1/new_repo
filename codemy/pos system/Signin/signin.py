from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        infom = self.ids.info

        uname = user.text
        pssw = pwd.text

        if uname == "" or pssw == "":
            infom.text = "[color=#ff0000]Username and/or Password required[/color]"
        else:
            if uname == 'admin' and pssw == 'admin':
                infom.text = "[color=#00ff00]Logged in successfully!!![/color]"
            else:
                infom.text = "[color=#ff0000]Invalid Username and/or Password[/color]"

class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    sa = SigninApp()
    sa.run()