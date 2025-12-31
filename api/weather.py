import requests

def get_weather(latitude, longitude):
    """
    Fetch current weather data from Open-Meteo API
    Returns temperature (°C), humidity (%), rainfall (mm)
    """

    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current=temperature_2m,relative_humidity_2m,precipitation"
    )

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch weather data")

    data = response.json()["current"]

    weather = {
        "temperature": data["temperature_2m"],
        "humidity": data["relative_humidity_2m"],
        "rainfall": data["precipitation"]
    }

    return weather


# Test the function
if __name__ == "__main__":
    # Example: Bengaluru
    weather = get_weather(12.9716, 77.5946)
    print(weather)
