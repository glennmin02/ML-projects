import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QLineEdit, QPushButton {
                font-family: Poppins;
            }
            QLabel#city_label{
                font-size: 24px;
                font-style: bold;
            }
            QLineEdit#city_input {
                font-size: 22px;
                padding: 8px;
                border: 2px solid #ccc;
                border-radius: 10px;
            }
            QPushButton#get_weather_button {
                font-size: 22px;
                background-color: #007BFF;
                color: white;
                padding: 5px;
                border: none;
                border-radius: 5px;
            }
            QLabel#temperature_label {
                font-size: 22px;
            }
            QLabel#emoji_label {
                font-size: 64px;
                font-family: Apple Color Emoji, Segoe UI Emoji, NotoColorEmoji, Android Emoji, EmojiSymbols;
            }
            QLabel#description_label {
                font-size: 22px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        api_key = "8a9052cf0ef20137d79c34e67f7fedb6"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request. Please check the city name.")
                case 401:
                    self.display_error("Invalid API key. Please check your API key.")
                case 403:
                    self.display_error("Access forbidden. You might not have permission to access this resource.")
                case 404:
                    self.display_error("City not found. Please check the city name.")
                case 500:
                    self.display_error("Server error. Please try again later.")
                case 502:
                    self.display_error("Bad gateway. Please try again later.")
                case 503:
                    self.display_error("Service unavailable. Please try again later.")
                case 504:
                    self.display_error("Gateway timeout. Please try again later.")
                case _:
                    self.display_error(f"An unexpected error occurred. Please try again later. Code: {http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error. Please try again later.")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error. Please try again later.")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects error. Please try again later.")
        except requests.exceptions.RequestException:
            self.display_error("Connection error. Please try again later.")

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 20px; font-style: regular; color: red;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        temperature_k = data["main"]["temp"]
        temperature_celsius = temperature_k - 273.15
        weather_description = data["weather"][0]["description"]
        weather_id = data["weather"][0]["id"]
        self.temperature_label.setStyleSheet("font-size: 22px; font-style: regular; color: black;")
        self.temperature_label.setText(f"{temperature_celsius:.0f} ºC")
        self.description_label.setText(f"{weather_description}")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))

    @staticmethod
    def get_weather_emoji(weather_id):
        match weather_id:
            case id if 200 <= id < 300:
                return "⛈️"  # Thunderstorm
            case id if 300 <= id < 400:
                return "🌦️"  # Drizzle
            case id if 500 <= id < 600:
                return "🌧️"  # Rain
            case id if 600 <= id < 700:
                return "❄️"  # Snow
            case id if 700 <= id < 800:
                return "🌫️"  # Atmosphere (fog, mist, etc.)
            case 800:
                return "☀️"  # Clear
            case id if 801 <= id < 900:
                return "☁️"  # Clouds
            case _:
                return "🌈"  # Default/Unknown

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())