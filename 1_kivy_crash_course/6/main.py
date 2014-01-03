from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import random
from kivy.properties import ListProperty


class ScatterTextWidget(BoxLayout):
    text_colour = ListProperty([1, 0, 0, 1])

    def change_label_colour(self):
        colour = [random() for i in range(3)] + [1]
        self.text_colour = colour

    # You can do this now, since this is a real Kivy property!
    def on_text_colour(self, *args, **kwargs):
        pass


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
