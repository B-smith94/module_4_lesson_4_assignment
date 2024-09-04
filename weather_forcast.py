#Task 1
def fetch_weather_data(city):
    print(f"Fetching weather data for {city}...")
    weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
    return weather_data.get(city, {})

def parse_weather_data(data):
    if not data:
        return "Weather data not available"
    city = data["city"]
    temperature = data["temperature"]
    condition = data["condition"]
    humidity = data["humidity"]
    return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

def display_weather(city):
    data = fetch_weather_data(city)
    if not data:
        print(f"Weather data not available for {city}")
    else:
        return parse_weather_data(data)

def main():
    while True:
        city = input("Enter the city to get the weather forcast or 'exit' to quit: ").title()
        if city == 'Exit':
            break
        else:
            forecast = display_weather(city)
        print(forecast)

if __name__ == "__main__":
    main()