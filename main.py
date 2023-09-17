from taipy import Gui
from taipy.gui import Html
from weatherNWS import get_weather
from ultravioletInfo import get_uv_sun_info
from datetime import datetime

day_forecast, night_forecast = get_weather()

# Get and print the required weather information for the day
temperature_day = day_forecast["temperature"]
wind_speed_day = day_forecast["windSpeed"]
short_forecast_day = day_forecast["shortForecast"]

dayForecastSummary = (f"Day Forecast: Temperature: {temperature_day} °F, Wind Speed: {wind_speed_day}, Description: {short_forecast_day}")
print(dayForecastSummary)

# Get and print the required weather information for the night
temperature_night = night_forecast["temperature"]
wind_speed_night = night_forecast["windSpeed"]
short_forecast_night = night_forecast["shortForecast"]

nightForecastSummary = (f"Night Forecast: Temperature: {temperature_night} °F, Wind Speed: {wind_speed_night}, Description: {short_forecast_night}")
print(nightForecastSummary)

# Get the current date and time
current_datetime = datetime.now()

# Format it as a string in "hh:mm" format
current_time_str = current_datetime.strftime("%H:%M")

print(current_time_str)

# use location 
last_updated = current_time_str
temperature = "92 °F"
humidity = "39%"
wind_speed = "10 MPH (Low)"
wave_conditions = "Green Flag"
marine_life = "See Local Guidelines"
facilities = "Showers/Restrooms: Yes"
water_fountain = "Yes"

feed_link = "https://v.angelcam.com/iframe?v=6xbymjk4y2&autoplay=1"
feed_name = "Live feed- SoBe Dive Shop"

# remember to pass lat, lng, alt, dt and your token
info = get_uv_sun_info(25.80, -80.13, 100, '', 'openuv-getyourown-io')

uv = info['uv']
sunrise = info['sunrise']
sunset = info['sunset']

print(info)
print(f"UV Index: {uv}, Sunrise Time: {sunrise}, Sunset Time: {sunset}")

html_page = Html("""
<h1>Miami Beach conditions</h1>
<h2>Daily Report (general area):</h2>
<p>Last updated: <taipy:text> {last_updated}</taipy:text></p>
<h3><taipy:text>{dayForecastSummary}</taipy:text></h3>
<h3><taipy:text>{nightForecastSummary}</taipy:text></h3>

<table>
  <tr>
    <th>Category</th>
    <th>Info</th>
  </tr>
  <tr>
    <td>UV Index</td>
    <td><taipy:text>{uv}</taipy:text></td>
  </tr>
  </table>
<h3>Wind Speed, Wave Height &amp; Swimming Difficulty</h3>
<p><b>Moderate Breeze (8-12 MPH)</b>, Wave Height: Small waves developing, Swimming Difficulty: More difficult, caution for novice swimmers</p>
<p>Fresh Breeze (13-18 MPH), Wave Height: Moderate waves of more pronounced long form, Swimming Difficulty: Difficult, only seasoned swimmers should explore</p>
<p>Strong Breeze (19-24 MPH), Wave Height: Large waves, foam starts to spray, Swimming Difficulty: Very difficult, rescue likely needed</p>
<p>Near Gale (25-31 MPH), Wave Height: Sea heaps up, foam from breaking waves, Swimming Difficulty: Extremely perilous past this</p>

<p>High UV &amp; temp call for sunscreen &amp; hydration. Consider wind speed &amp; flags before swimming!</p>
<iframe src="https://v.angelcam.com/iframe?v=6xbymjk4y2&autoplay=1"></iframe>
<p>Live feed- SoBe Dive Shop</p>
<a href="https://www.miamibeachfl.gov/egovapp/beachconditions/">More information: MiamiBeach Online</a>
""")

Gui(page=html_page).run()
