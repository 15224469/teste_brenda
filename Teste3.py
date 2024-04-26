from kivy.app import App
from kivy.uix.label import Label 

class MinhaApp(App):
    def build (self):
        return Label(
            text='Jhonathan é careca',
            halign='left', # Alinha o texto à esquerda
            valign='top' #alinha o texto no topo
        )
    
if _name_ == "_main_ ":
    MinhaApp().run()