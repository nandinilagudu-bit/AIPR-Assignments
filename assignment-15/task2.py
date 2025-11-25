import requests
import json

def display_weather(city_name):
    try:
        api_key = "bcf8e39a943d27dd070b0e78165fbfe6"   # Replace with your OpenWeatherMap API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)

        # Convert response to JSON
        weather_data = response.json()

        # ----------- CITY NOT FOUND CHECK -------------
        if weather_data.get("cod") == "404":
            print("\nCity not found! Please check spelling.")
            return
        # -----------------------------------------------

        # If API returned any other error (e.g., invalid key)
        if weather_data.get("cod") != 200:
            print("\nAPI Error:")
            print(json.dumps(weather_data, indent=4))
            return

        # Print pretty JSON output
        print("\nWeather Details (JSON Output):")
        print(json.dumps(weather_data, indent=4))

    except requests.exceptions.ConnectionError:
        print("Network Error: Unable to connect to the API.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except Exception as e:
        print("An error occurred:", str(e))


# Example usage
city = input("Enter city name: ")
display_weather(city)