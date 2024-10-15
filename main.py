from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.size = (310, 580)

def rgba(hex_str):
    return get_color_from_hex(hex_str)

class Rms(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        return screen_manager

if __name__ == "__main__":
      
    
    LabelBase.register(name="MPoppins", fn_regular="fonts/Poppins-Medium.ttf")
    LabelBase.register(name="BPoppins", fn_regular="fonts/Poppins-SemiBold.ttf")


    Rms().run()
