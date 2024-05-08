from kivy.app import App 
from kivy.uix.label import Label
from kivy.core.window import Window 

class MinhaApp(App):
    def build(self):
        Window.clearcolor = ('f74780')
        label = Label(text='Esta é uma tela com fundo Rosa',color=('1d44b8'))

        return label

if __name__ == "__main__":
    MinhaApp().run()