import unittest

from sys import path 
path.append("../../")

from project.src.model.request import Request

class Test_request(unittest.TestCase):

    def test_requestBycoord(self):
        request = Request('7d70278055ea48aaad00a7761fbde797')
        result = request.requestByCoord('abc, def')
        self.assertEqual(result,"Algo salió mal\n")
        result = request.requestByCoord('4.70159, -74.1469')
        result = result.split("\n")
        self.assertEqual(result[0], "Villa Mejía")

    def test_requestsByName(self):
        request = Request('7d70278055ea48aaad00a7761fbde797')
        result = request.requestsByName('123,')
        self.assertEqual(result,"Algo salió mal\n")
        result = request.requestsByName('Ciudad de México')
        result = result.split("\n")
        self.assertEqual(result[0],"Ciudad de México")
        self.assertEqual(result[4],"Coords:\t19.4285, -99.1277")


    if __name__ =='__main__':
        unittest.main()

