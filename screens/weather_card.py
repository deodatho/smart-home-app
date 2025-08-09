from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivy.clock import Clock
import random
# nosec: B311
class WeatherCard(MDCard):
    weather_icon = StringProperty("weather-sunny")
    weather_status = StringProperty("Ensolarado")
    temperature = StringProperty("28°C")
    rain_info = StringProperty("Baixa probabilidade de chuva")
# nosec: B311
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_weather()
        Clock.schedule_interval(self.update_weather, 60)
# nosec: B311
    def update_weather(self, *args):
        weather_options = [
            {"icon": "weather-sunny", "status": "Ensolarado", "temp": f"{random.randint(25, 35)}°C", "rain": "Sem chuva"},
            {"icon": "weather-partly-cloudy", "status": "Parcialmente nublado", "temp": f"{random.randint(20, 25)}°C", "rain": "Baixa probabilidade de chuva"},
            {"icon": "weather-cloudy", "status": "Nublado", "temp": f"{random.randint(18, 22)}°C", "rain": "Possibilidade de chuva"},
            {"icon": "weather-rainy", "status": "Chuvoso", "temp": f"{random.randint(15, 20)}°C", "rain": "Chuva prevista"}, # nosec: B311
        ]
        weather = random.choice(weather_options)
        self.weather_icon = weather["icon"]
        self.weather_status = weather["status"]
        self.temperature = weather["temp"]
        self.rain_info = weather["rain"]
# nosec: B311
    def manual_window_control(self):
        from kivymd.app import MDApp
        app = MDApp.get_running_app()
        app.root.get_screen("home").show_window_control_dialog()
# nosec: B311