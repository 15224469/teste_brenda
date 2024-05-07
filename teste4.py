from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RotuloApp(App):
    def build(self):
        Layout = BoxLayout(orientation='vertical')
        self.lab1 = Label(
            text='EU', color=('fa8fb1'),
            font_size=40, bold=True
    )
        
        self.lab2 = Label(
            text= 'AMO', color= ('fc6998'),
            font_size=40, italic= True
    )
        
        self.lab3 = Label(
            text= 'ROSA', color=('e0218a'),
            font_size=40, font_name= 'Georgia',
            underline= True
    )
        
        Layout.add_widget(self.lab1)
        Layout.add_widget(self.lab2)
        Layout.add_widget(self.lab3)
        return Layout
    
if __name__ == '__main__':
    RotuloApp().run()