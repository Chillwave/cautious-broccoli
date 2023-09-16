from taipy import Gui

page = """
# Weather Man 365

Wind speed: <|{windowSpeed}|> \n
Wind direction: <|{windDirection}|> \n
Current temp (F): <|{temp}|> \n
Humidity in %: <|{humidity}|> \n


"""

temp = 80
humidity = 90
windDirection = "North"
windSpeed = 14
Gui(page=page).run() # use_reloader=True