import requests

def display_weather_details(city_name):
    try:
        api_key = "bcf8e39a943d27dd070b0e78165fbfe6"   # Replace with your API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)
        weather_data = response.json()

        # If city name is wrong
        if weather_data.get("cod") == "404":
            print("\nCity not found! Please check spelling.")
            return

        # Extract specific fields
        city = weather_data["name"]
        temp = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        # Display clean output
        print("\n--- Weather Details ---")
        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except Exception as e:
        print("Error:", str(e))


# Example usage
city = input("Enter city name: ")
display_weather_details(city)