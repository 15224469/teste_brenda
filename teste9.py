from kivy.app import App
from kivy.uix.image import Image,  AsyncImage

class MinhaApp(App):
    def build(self):
        return AsyncImage(source='https://recreio.uol.com.br/media/_versions/disney/enrolados_capa_widelg.jpg')

if __name__ == "__main__":
    MinhaApp().run()