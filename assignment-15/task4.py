import requests

def get_weather(city_name):
    try:
        api_key = "bcf8e39a943d27dd070b0e78165fbfe6"   # Replace with real API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        # If city name invalid
        if data.get("cod") == "404":
            print("Error: City not found. Please enter a valid city.")
            return

        # Extract fields
        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Output
        print(f"\nCity: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except Exception as e:
        print("Something went wrong:", str(e))


# Ask user for input
city = input("Enter city name: ")
get_weather(city)