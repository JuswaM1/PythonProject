import requests

def get_weather(city):
    api_key = "API"  
    base_url = "weather link"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data.get("cod") == 200: 
            weather = data["weather"][0]["description"].capitalize()
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            print(f"\n--- Weather in {city.capitalize()} ---")
            print(f"Weather: {weather}")
            print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"City '{city}' not found. Please try again.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


def main():
    print("Welcome to the Weather App!")
    while True:
        city = input("\nEnter the city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break
        elif city:
            get_weather(city)
        else:
            print("Please enter a valid city name.")


if __name__ == "__main__":
    main()
