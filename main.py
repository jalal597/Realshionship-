from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import hashlib

class LoveCalculator(App):

    def build(self):
        self.layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        title = Label(
            text="❤️ LOVE CALCULATOR ❤️",
            font_size=28
        )

        self.name1 = TextInput(
            hint_text="Enter Your Name",
            multiline=False
        )

        self.name2 = TextInput(
            hint_text="Enter Partner Name",
            multiline=False
        )

        btn = Button(
            text="❤️ Check Love ❤️",
            size_hint=(1, 0.25)
        )
        btn.bind(on_press=self.check)

        self.result = Label(
            text="",
            font_size=22
        )

        self.layout.add_widget(title)
        self.layout.add_widget(self.name1)
        self.layout.add_widget(self.name2)
        self.layout.add_widget(btn)
        self.layout.add_widget(self.result)

        return self.layout

    def check(self, instance):
        n1 = self.name1.text.strip()
        n2 = self.name2.text.strip()

        if not n1 or not n2:
            self.result.text = "⚠️ Enter both names!"
            return

        pair = "-".join(sorted([n1.lower(), n2.lower()]))

        h = hashlib.md5(pair.encode()).hexdigest()
        percentage = int(h[:8], 16) % 101

        if percentage >= 90:
            msg = "💖 Perfect Match!"
        elif percentage >= 70:
            msg = "😍 Very Good Match!"
        elif percentage >= 50:
            msg = "😊 Average Match!"
        else:
            msg = "🤝 Better as Friends!"

        self.result.text = (
            f"{n1} ❤️ {n2}\n\n"
            f"{percentage}%\n"
            f"{msg}"
        )

LoveCalculator().run()
