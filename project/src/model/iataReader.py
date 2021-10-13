import csv

class IataReader:
    iataCodes = {}

    def getIata(self, code):
        """Finds the complete city name in airport-codes.csv file given
        the city iata code and returns it.
        Args:
            code: city iata code.
        Returns:
            city: Real name city.
        """
        if code in self.iataCodes:
            return self.iataCodes[code]
        return "Invalid city"

    def iatasCodes(self):
        """Creates a dictionary with all the city iata codes
        and its complete name by reading the airport-codes.csv file.
        Returns:
            data: A dictionary with the city iata codes and its complete name.
        """
        data = {}
        with open("project/data/airport-codes.csv", newline= '') as coord:
            lines = csv.DictReader(coord)
            for line in lines:
                if line['iata_code'] == '':
                    continue
                else:
                    data[line['iata_code']] = line['municipality']
        return data

    def __init__(self):
        """iataReader constructor.
        """
        self.iataCodes = self.iatasCodes()