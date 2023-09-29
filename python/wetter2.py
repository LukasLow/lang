import requests
import json

def get_weather(city):
    api_key = "DEIN_API_KEY_HIER_EINFUEGEN"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
    complete_url = base_url + "q=" + city + "&appid=" + api_key
  
    response = requests.get(complete_url)
  
    if response.status_code == 200:
        data = response.json()
      
        main_data = data['main']
        temp = main_data['temp'] - 273.15  # Umwandlung von Kelvin in Celsius
      
        weather_data = data['weather']
        weather_description = weather_data[0]['description']
      
        print(f"Wetter in {city}:")
        print(f"Temperatur: {temp:.2f}°C")
        print(f"Beschreibung: {weather_description}")
      
    else:
        print("Stadt nicht gefunden.")

# Hauptprogramm
if __name__ == "__main__":
    city = input("Gib den Namen der Stadt ein: ")
    get_weather(city)
