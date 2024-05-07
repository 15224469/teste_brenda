from kivy.app import App
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex

def botao_pressionado(instance):
    print("botao_pressionado")

class MinhaApp(App):
    def build(self):
        btn = Button(text='Clique Aqui',font_size=50, font_name='Georgia', background_color=get_color_from_hex('70b450'), size_hint=(0.6, 0.2))
        btn.bind(on_press=botao_pressionado)
        return btn
    
if __name__ == "__main__":
    MinhaApp().run()