import random
import sys
import json
import requests

API_key = "9e5700429c16e0e07fe7ea27825fc13a"

FIRST_LAYER_HOT_WEATHER = ["T-shirt", "Tanktop", "Crop top"]
SECOND_LAYER_HOT_WEATHER = ["Cardigan", "Hoodie"]
FIRST_LAYER_COLD_WEATHER = ["Long sleeve", "Chunky Sweater", "Turtle neck"]
SECOND_LAYER_COLD_WEATHER = ["Winter coat", "Fleece vest"]
HOT_WEATHER_BOTTOMS = ["Shorts", "Skirt", "Linen pants"]
COLD_WEATHER_BOTTOMS = ["Leggings", "Jeans", "Sweatpants"]


class assemble_outfit:
    def __init__(self):
        self.zip_code = str(sys.argv[1])
        self.top = ''
        self.bottom = ''
        self.number_of_layers = 0
        self.fahrenheit = 0
        self.celsius = 0
        self.kelvin = 0

    # Get data from the API
    def get_API_data(self):
        API_url = 'http://api.openweathermap.org/data/2.5/weather?zip={}&appid={}'.format(self.zip_code, API_key)
        data = requests.get(API_url)
        dictionary = data.json()
        self.kelvin = dictionary['main']['feels_like']

    # Convert kelvin to fahrenheit and celsius
    def kelvin_conversions(self):
        self.get_API_data()
        self.fahrenheit = (self.kelvin - 273.15) * 9 / 5 + 32
        self.celsius = self.kelvin - 273.15

    # Calculate how many layers we will be needing
    def layers(self):
        if self.fahrenheit >= 77 or (50 <= self.fahrenheit <= 60):
            self.number_of_layers = 1
        elif (60 < self.fahrenheit < 77) or (35 <= self.fahrenheit < 50):
            self.number_of_layers = 2
        else:
            self.number_of_layers = 3

    # Recommend me a top to wear based on the temperature
    def top_recommendation(self):
        if self.number_of_layers == 1 and self.fahrenheit >= 77:
            self.top = "A " + random.choice(FIRST_LAYER_HOT_WEATHER)
        elif self.number_of_layers == 1 and (50 <= self.fahrenheit <= 60):
            self.top = "A " + random.choice(FIRST_LAYER_COLD_WEATHER)
        elif self.number_of_layers == 2 and (60 < self.fahrenheit < 77):
            self.top = "A " + random.choice(FIRST_LAYER_HOT_WEATHER) + " and a " \
                       + random.choice(SECOND_LAYER_COLD_WEATHER)
        elif self.number_of_layers == 2 and (35 <= self.fahrenheit < 50):
            self.top = "A " + random.choice(FIRST_LAYER_COLD_WEATHER) + " and a " \
                       + random.choice(SECOND_LAYER_COLD_WEATHER)
        else:
            self.top = "Wear thermal underwear, a " + \
                       random.choice(FIRST_LAYER_COLD_WEATHER) + ", and a " \
                       + random.choice(SECOND_LAYER_COLD_WEATHER)

    # Recommend me a bottom to wear based on the temperature
    def bottoms_recommendation(self):
        if self.fahrenheit > 60:
            self.bottom = random.choice(HOT_WEATHER_BOTTOMS)
        else:
            self.bottom = random.choice(COLD_WEATHER_BOTTOMS)

    # Print out my recommendations
    def give_me_an_outfit(self):
        self.get_API_data()
        self.kelvin_conversions()
        self.layers()
        self.top_recommendation()
        self.bottoms_recommendation()
        print("The temperature feels like: " + str(self.fahrenheit) + " F or " +
              str(self.celsius) + " C")
        print("You should wear " + str(self.number_of_layers) + " layer(s):")
        print(self.top + " on top and " + self.bottom + " on the bottom")


outfit = assemble_outfit()
outfit.give_me_an_outfit()
