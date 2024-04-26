from kivy.app import App 
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Label(text='Brendinha s2', font_size=50, font_name='Georgia', color= get_color_from_hex('fc6998'))
    
if __name__ == "__main__":
    MinhaApp().run()