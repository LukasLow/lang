import requests

def get_weather(city):
    base_url = f"https://wttr.in/{city}?format=3"
  
    try:
        response = requests.get(base_url)
      
        if response.status_code == 200:
            print(f"Wetter in {city}: {response.text}")
      
        else:
            print("Stadt nicht gefunden oder Serverfehler.")
            
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

# Hauptprogramm
if __name__ == "__main__":
    city = input("Gib den Namen der Stadt ein: ")
    get_weather(city)
