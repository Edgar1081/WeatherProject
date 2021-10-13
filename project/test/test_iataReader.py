import unittest
from sys import path 
path.append("../../")

from project.src.model.iataReader import IataReader

class Test_iataReaer(unittest.TestCase):

    def test_getIata(self):
        code = IataReader()
        self.assertEqual(code.getIata('123'), 'Invalid city')
        self.assertEqual(code.getIata('BOG'),'Bogota')

    if __name__ =='__main__':
        unittest.main()