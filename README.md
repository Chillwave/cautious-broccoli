


# Miami Beach Conditions Reporting
# "My Job is Just Beach"
## ShellHacks 2023 - submission

###  Best Use of Taipy
- Taipy is a powerful yet easy to use open-source Python library for creating full stack web applications! If you’re a Python developer, this library enables you to build interactive and dynamic graphical user interfaces and support them with data-driven backends. All of these functionalities are just a pip install taipy away and can cut your development time in half! Use Taipy in your hackathon project for a chance to win a set of JBL Wireless Headphones for you and each of your team members, as well as a chance to have your project featured on the Taipy website!

This Python script helps retrieve and present weather and beach conditions for Miami Beach. 

## Features

- Fetches current UV index, sunset and sunrise times from the OpenUV API.
- Fetches and displays current weather forecast from the weatherNWS module.
- Displays the fetched condition data into a HTML page generated using the taipy.Gui library.

## Usage

Please input your own API token for OpenUV in the function call to `get_uv_sun_info()` like so:

```python
info = get_uv_sun_info(25.80, -80.13, 100, '', '<Your-Token-Here>')
```

The script prints out daily and nightly forecasts, along with current time. It also outputs a table with UV Index for the Miami Beach conditions and provides additional information about the beach condition.

It also hosts a live feed from SoBe Dive Shop, and links back to Miami Beach's official site for more comprehensive information. [More Info](https://www.miamibeachfl.gov/egovapp/beachconditions/)

_Note:_ You'll need access to the `taipy`, `weatherNWS`, and `ultravioletInfo` modules, and ensure that all dependencies in those modules are also installed and operationally set up for correct execution.

---

## Beach Conditions

It provides current air temperature, wind speed and the overall forecast for the day and night. The last update time is also recorded and displayed.

Wind speed, wave height, and swimming difficulties are also noted. Information such as the current UV index, temperature, and wind speed is used to provide advice about whether sun protection is necessary or whether novice swimmers should attempt to swim.
