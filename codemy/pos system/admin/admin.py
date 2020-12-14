from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from collections import OrderedDict
from pymongo import MongoClient


class AdminWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        stb = {
            "THO": {0: "St0", 1: 'Sample1', 2: 'Sample2', 3: 'Sample4'},
            "TH1": {0: "Stm0", 1: "Sample1", 2: "Sample2", 3: "Sample4"},
            "TH2": {0: "Stmp0", 1: "Sampled1.0", 2: "Sampled2.0", 3: "Sample4.0"},
            "TH3": {0: "Stmpl0", 1: 'Sample1', 2: 'Sample2', 3: "Sample4"},
            "TH4": {0: 'Stmple0', 1: "Sample1", 2: "Sample2", 3: "Sample4"}
        }
        print(self.get_products())

    def get_users(self):
        client = MongoClient()
        db = client.silverpos
        users = db.users
        _users = OrderedDict(
            first_name={},
            last_name={},
            user_name={},
            passwords={},
            designations={}
        )
        first_name = []
        last_name = []
        user_name = []
        passwords = []
        designations = []

        for user in users.find():
            first_name.append(user['first_name'])
            last_name.append(user['last_name'])
            user_name.append(user['user_name'])
            passwords.append(user['password'])
            designations.append(user['designation'])
        # print(designations)
        user_length = len(first_name)
        idx = 0
        while idx < user_length:
            _users['first_name'][idx] = first_name[idx]
            _users['last_name'][idx] = last_name[idx]
            _users['user_name'][idx] = user_name[idx]
            _users['passwords'][idx] = passwords[idx]
            _users['designations'][idx] = designations[idx]

            idx += 1
        return _users


class AdminApp(App):
    def build(self):
        return AdminWindow()


if __name__ == "__main__":
    AdminApp().run()
