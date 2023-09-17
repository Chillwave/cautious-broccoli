import requests

def get_weather():
    # Request headers
    headers = {
        'User-Agent': '(Your_Application_Info)',
    }

    # Specify the office and grid X, Y for Miami Beach
    office = "MFL"
    gridX = "112"
    gridY = "52"

    # API Endpoint
    forecast_endpoint = f"https://api.weather.gov/gridpoints/{office}/{gridX},{gridY}/forecast"

    # Make a get request to the API
    resp = requests.get(forecast_endpoint, headers=headers)

    # Converting the response to JSON
    data = resp.json()

    # Fetch day and night weather forecasts
    day_forecast = data['properties']['periods'][0]
    night_forecast = data['properties']['periods'][1]

    return day_forecast, night_forecast
