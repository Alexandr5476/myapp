from kivy.app import App
# from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import telegram

Window.title = "Программа"


class My(App):

    def __init__(self):
        super().__init__()
        self.input = TextInput(hint_text="Пароль", multiline=False)
        self.button = Button(text="Кнопочка")
        self.button.bind(on_press=self.from_input)

    def from_input(self, *args):
        data = self.input.text
        telegram.send(data)

    def press(self, *args):
        print("Нажато")

    def build(self):
        box = BoxLayout(orientation='vertical')
        # label = Label(text="Программа работает")
        # box.add_widget(label)
        box.add_widget(self.input)
        box.add_widget(self.button)
        return box


if __name__ == '__main__':
    My().run()
