import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']
        
        print(f"City: {data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("Error fetching data from OpenWeatherMap API")

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, api_key)
