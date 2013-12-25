from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput


class TutorialApp(App):
    def build(self):
        layout_main = BoxLayout(
            orientation='vertical',

        )
        text_input = TextInput(
            font_size=150,
            height=200,
            size_hint_y=None,
            text='default',
        )

        layout = FloatLayout()
        scatter = Scatter()
        label = Label(
            text="default",
            font_size=150,
        )

        text_input.bind(text=label.setter('text'))

        layout.add_widget(scatter)
        scatter.add_widget(label)

        # Order is important - first is top/left
        layout_main.add_widget(text_input)
        layout_main.add_widget(layout)

        return layout_main


if __name__ == "__main__":
    TutorialApp().run()
