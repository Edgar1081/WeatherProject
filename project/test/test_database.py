import unittest
from sys import path
path.append("../..")
from project.src.model.database import DataBase
from project.src.model.request import Request

class Test_database(unittest.TestCase):
    def test_formatPrint(self):
        dictionary = {0:{'origin':'TLC', 'destination':'MTY'}}
        request = Request('7d70278055ea48aaad00a7761fbde797')
        database = DataBase(dictionary)
        database.fill(1)
        result = database.formatPrint("TLC", "MTY")
        result = result.split("\n")
        self.assertEqual(result[1],"ORIGEN:\tTLC")
        self.assertEqual(result[2],"DESTINO:\tMTY")
        

if __name__ =='__main__':
    unittest.main()
