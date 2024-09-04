#Task 1
class WeatherDataFetcher:
    def __init__(self, city):
        self.city = city

    def fetch_weather_data(city):
        print(f"Fetching weather data for {city}...")
        weather_data = {
                "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
                "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
                "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
            }
        return weather_data.get(city, {})

class DataParser(WeatherDataFetcher):
    def __init__(self, city):
        super().__init__(city)

    def parse_weather_data(weather_data):
        if not weather_data:
            return "Weather data not available"
        city = weather_data["city"]
        temperature = weather_data["temperature"]
        condition = weather_data["condition"]
        humidity = weather_data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def display_weather(city):
        data = WeatherDataFetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            return DataParser.parse_weather_data(data)

def main():
    while True:
        city = input("Enter the city to get the weather forcast or 'exit' to quit: ").title()
        if city == 'Exit':
            break
        else:
            forecast = DataParser.display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()