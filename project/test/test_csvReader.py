import unittest
from sys import path
path.append("../..")
from project.src.model.csvReader import CsvReader

class Test_csvreader(unittest.TestCase):

    def test_readCsv(self):
        dic ={0: {'id': '1', 'first_name': 'Georgia', 'last_name': 'Birtwell', 'gender': 'Female'}, 
                1: {'id': '2', 'first_name': 'Harvey', 'last_name': 'Francescone', 'gender': 'Male'}, 
                2: {'id': '3', 'first_name': 'Elysia', 'last_name': 'Ryall', 'gender': 'Female'}, 
                3: {'id': '4', 'first_name': 'Leta', 'last_name': 'April', 'gender': 'Female'}, 
                4: {'id': '5', 'first_name': 'Avril', 'last_name': 'Kullmann', 'gender': 'Female'},
                5: {'id': '6', 'first_name': 'Tyne', 'last_name': 'Dawton', 'gender': 'Female'}, 
                6: {'id': '7', 'first_name': 'Calli', 'last_name': 'Mc-Kerley', 'gender': 'Female'},
                7: {'id': '8', 'first_name': 'Selie', 'last_name': 'Reilingen', 'gender': 'Female'},
                8: {'id': '9', 'first_name': 'Sibylla', 'last_name': 'Mogra', 'gender': 'Female'}, 
                9: {'id': '10', 'first_name': 'Rockey', 'last_name': 'Bleaden', 'gender': 'Male'}}

        csv = CsvReader()
        dictionary = csv.readCsv('project/test/testCSV/csvReaderTest.csv')
        self.assertDictEqual(dictionary,dic)        

    if __name__ =='__main__':
        unittest.main()