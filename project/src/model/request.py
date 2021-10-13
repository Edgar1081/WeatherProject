import requests
import time
from .normalizer import Normalizer
class Request:

    key = ''
    url = "http://api.openweathermap.org/data/2.5/weather?"

    def __init__(self, key):
        """Request constructor
        Args:
            key: The API's key to make requests.
        """
        self.key = key

    def manageData(self, lat, lon, name, weather, temp, sens):
        """Auxiliar method that concatenates the recived information with a specific format.
        Args:
            lat: A string of City latitude.
            lon: A string of City longitude.
            name: A string of City name.
            weather: A string of City weather.
            temp: A string of City temperature.
            sens: A string of City thermal sensation.
        Returns:
            final: Concatenated strings with a specific format.
        """
        name = name + "\n"
        weather = 'Clima:\t{}\n'.format(weather)
        temp =    'Temp:\t{}°C\n'.format(temp)
        sens =    'Sensación térmica:\t{}°C\n'.format(sens)
        coords =  'Coords:\t{}, {}\n'.format(lat, lon)
        final = name + weather + temp + sens + coords
        return final

    def requestByCoord(self, coords):
        """Make a request by city coordinates and if it fails, return an error message.
        Args:
            coords: A string of city coordinates.
        Returns:
            string : A string with format of the request result.
        """
        answer = {}
        latlong = coords.split(', ')
        urlCoord = self.url + "lat={}&lon={}&appid={}".format(latlong[0], latlong[1], self.key)
        urlcomplete = urlCoord + "&units=metric&lang=es"
        answer = requests.get(urlcomplete).json()
        lat = latlong[0]
        lon = latlong[1]
        try:
            name = answer['name']
            weather = answer['weather'][0]['description'].upper()
            temp = answer['main']['temp']
            sens = answer['main']['feels_like']
            time.sleep(1)
        except KeyError:
            return "Algo salió mal\n"
        return self.manageData(lat, lon, name, weather, temp, sens)
        

    def requestsByName(self, name):
        """Make a request by city name and if it fails, return an error message.
        Args:
            name : A string of city name.
        Returns:
            string : A string with format of the request result.
        """
        answer = {}
        normalizer = Normalizer()
        normalizedName = normalizer.normalize(name)
        urlName = self.url + "q={}&appid={}".format(normalizedName, self.key)
        urlcomplete = urlName + "&units=metric&lang=es"
        answer = requests.get(urlcomplete).json()
        time.sleep(1)
        try:
            lat = str(answer['coord']['lat'])
            lon = str(answer['coord']['lon'])
            weather = answer['weather'][0]['description'].upper()
            temp = answer['main']['temp']
            sens = answer['main']['feels_like']
        except KeyError:
            return "Algo salió mal\n"
        return self.manageData(lat, lon, name, weather, temp, sens)
    
    
