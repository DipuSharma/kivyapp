from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutExample(BoxLayout):
    def __int__(self, **kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass
    # def build(self):
    #     return BoxLayoutExample()


home_app = TheLabApp()
if __name__ == '__main__':
    home_app.run()
