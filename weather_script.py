import requests

def fetch_weather(api_key: str, town: str, country_code: str = "us", units: str = "metric"):
    """
    Fetches current weather data for a specific town from OpenWeatherMap API.

    Args:
        api_key (str): Your OpenWeatherMap API key.
        town (str): Name of the town/city.
        country_code (str): Country code (default: "us").
        units (str): Units for temperature ("metric", "imperial", or "standard").

    Returns:
        dict: Weather data as returned by the API, or None if request fails.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{town},{country_code}",
        "appid": api_key,
        "units": units
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    API_KEY = "7eb53b12d66e468608a5997276ae556a"  # Replace with your OpenWeatherMap API key
    TOWN = "Freiburg"
    COUNTRY_CODE = "de"
    weather = fetch_weather(API_KEY, TOWN, COUNTRY_CODE)
    if weather:
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        feels_like = weather['main']['feels_like']
        temp_min = weather['main']['temp_min']
        temp_max = weather['main']['temp_max']
        print(f"Weather in {TOWN}:")
        print(f"  Condition: {description}")
        print(f"  Temperature: {temp}°C (feels like {feels_like}°C)")
        print(f"  Min/Max Temperature: {temp_min}°C / {temp_max}°C")
        print(f"  Humidity: {humidity}%")
    else:
        print("Failed to fetch weather data.")