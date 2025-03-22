import requests

API_KEY = ' '

def main():
    city_name = input("Enter the city name")
    base_url=f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city_name}"
    response = requests.get(base_url)
    weather_data = response.json()
    print(weather_data)