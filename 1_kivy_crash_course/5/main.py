from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from random import random


class ScatterTextWidget(BoxLayout):
    def change_label_colour(self):
        colour = [random() for i in range(3)] + [1]
        self.ids['label_copy'].color = colour


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
