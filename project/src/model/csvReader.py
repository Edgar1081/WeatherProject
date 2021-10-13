import csv
import doctest
class CsvReader:

    def readCsv(self, route):
        """Returns a dictionary with all the lines reading the 
        dataset given in the file route.
        Args:
            route: The file route with the dataset.
        Returns:
            data:  A dictionary with all the lines in the dataset file.
        """
        i = 0
        data = {}
        with open(route) as csvfile:
            lines = csv.DictReader(csvfile)
            for line in lines:
                data[i] = line
                i = i + 1
        return data
