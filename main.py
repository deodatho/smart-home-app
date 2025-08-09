from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.screenmanager import MDScreenManager

from screens.login import LoginScreen
from screens.register import RegisterScreen 
from screens.home import HomeScreen
from screens.weather_card import WeatherCard 

Window.size = (360, 640)
class SmartHomeApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Amber"
        self.theme_cls.theme_style = "Light"

        Builder.load_file("smart_home.kv")

        sm = MDScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(RegisterScreen(name="register"))
        sm.add_widget(HomeScreen(name="home"))

        return sm

if __name__ == "__main__":
    SmartHomeApp().run()
