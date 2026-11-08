
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class PyTunes(App):
    def build(self):
        layout = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=15
        )

        layout.add_widget(Label(
            text="[b]PyTunes[/b]",
            markup=True,
            font_size=38
        ))

        layout.add_widget(Label(
            text="Your personal music player",
            font_size=18
        ))

        for name in ["MY MUSIC", "PLAY", "PAUSE", "PLAYLISTS"]:
            layout.add_widget(Button(
                text=name,
                font_size=20
            ))

        return layout


PyTunes().run()
