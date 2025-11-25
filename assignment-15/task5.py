import requests
import json
import os

def get_weather(city_name):
    try:
        api_key = "bcf8e39a943d27dd070b0e78165fbfe6" # Replace with your valid API key
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        params = {
            'q': city_name,
            'appid': api_key,
            'units': 'metric'
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        # Error: invalid city
        if data.get("cod") == "404":
            print("Error: City not found. Please enter a valid city.")
            return

        # Extract useful fields
        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Print formatted output
        weather_details = {
            "city": city,
            "temperature": temp,
            "humidity": humidity,
            "weather": description
        }

        print("\nWeather Details (JSON Output):")
        print(json.dumps(weather_details, indent=4))

        # --------------------------
        # Save output to Assignment15 folder
        # --------------------------
        file_name = r"C:\Users\BHANU NEEMKAR\OneDrive\Desktop\AIAP\assignment-15\t5.txt"

        # Append mode
        with open(file_name, "a") as file:
            file.write(json.dumps(weather_details) + "\n")

        print(f"\nWeather details saved to {file_name}")

    except Exception as e:
        print("An error occurred:", str(e))


# Example usage
city = input("Enter city name: ")
get_weather(city)