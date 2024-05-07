from kivy.app import App
from kivy.uix.video import Video

class MinhaApp(App):
    def build(self):
        return Video (source='https://youtu.be/iWlun5tWZDA?si=0v03myrhVNqTJPSt')
    
if __name__ == "__main__":
    MinhaApp().run()