from kivy.app import App
from kivy.uix.label import Label 

class MinhaApp(App):
    def build (self):
        return Label(
            text='Jhonathan é careca',
            font_size=50, 
            font_name='Georgia',
            halign='left', # Alinha o texto à esquerda
            valign='top', #alinha o texto no topo
            size_hint=(None, None), #Desativa o ajuste automático de tamanho
            size= (550, 1850), #Define o tamanho do rótulon
            text_size=(450, None) #Define a largura máxima do texto
        )
    
if __name__ == "__main__":
    MinhaApp().run()