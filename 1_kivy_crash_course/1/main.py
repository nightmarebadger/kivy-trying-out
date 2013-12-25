from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


class TutorialApp(App):
    def build(self):
        layout = FloatLayout()
        scatter = Scatter()
        label = Label(text="Hello world!",
                      font_size=150)

        layout.add_widget(scatter)
        scatter.add_widget(label)

        return layout


if __name__ == "__main__":
    TutorialApp().run()
