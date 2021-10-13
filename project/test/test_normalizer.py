import unittest
from sys import path 
path.append("../../")

from project.src.model.normalizer import Normalizer

class Test_normalize(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(Normalizer().normalize('Shūkat aş Şūfī'),'Shukat as Sufi')
        self.assertEqual(Normalizer().normalize('1235@_/'),'')

    if __name__ == "__main__":
        unittest.main()
