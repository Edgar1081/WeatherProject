import unicodedata
import re

class Normalizer:

    def normalize(self, string):
        """Returns a normalized String with NFKD format.
        Args:
            string: The string to normalize.
        Returns:
            normalizedString:  The string normalized using NFKD format.
        """
        stringNFKD = unicodedata.normalize('NFKD', string)
        normalizedString = re.sub('[^A-Za-z ]+', '', stringNFKD)
        return normalizedString

    
