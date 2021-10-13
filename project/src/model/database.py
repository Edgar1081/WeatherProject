from .request import Request
from .normalizer import Normalizer
from .iataReader import IataReader
class DataBase:
    data = {}
    cache = {}

    def case1(self, iata, request):
        """Auxiliar method used to manage dataset1, requesting by name
        each line in the datset1 and saving it in "cache".
        Args:
            iata: Auxiliar object to find the iata codes of each city in
            dataset1.
            request: Object to make requests.
        """
        for line in self.data:
            string1 = iata.getIata(self.data[line]['origin'])
            string2 = iata.getIata(self.data[line]['destination'])
            if not string1 in self.cache:
                self.cache[string1] = request.requestsByName(string1)
            if not string2 in self.cache:
                self.cache[string2] = request.requestsByName(string2)
            self.formatPrint(self.cache[string1], self.cache[string2])
                

    def case2(self,request):
        """Auxiliar method used to manage dataset2, requesting by name
        each line in the datset2 and saving it in "cache".
        Args:
            request: Object to make requests.
        """
        string1 = 'Ciudad de México'
        self.cache[string1] = request.requestsByName(string1)
        for line in self.data:
            string2 = self.data[line]['destino']
            if not string2  in self.cache:
                self.cache[string2] = request.requestsByName(string2)
            self.formatPrint(self.cache[string1], self.cache[string2])
    

    def fill(self, case):
        """Fills the "cache" dictionary requesting all the lines in "data"
        while using "case1" or "case2" to print the requests.
        Args:
            case: The specific dataset case.
        """
        if case == 1:
            request = Request('7d70278055ea48aaad00a7761fbde797')
            iata = IataReader()
            self.case1(iata, request)
        else:
            request = Request('3b84ee2fdcf2467e03e5eb24228ef6f2')
            self.case2(request)


    def formatPrint(self, string1, string2):
        """Auxiliar method used to print the requests information saved in
        "cache" dictionary.
        Args:
            string1 : Origin request information in "cache".
            string2 : Destiny request information in "cache".
        """
        ticket = '-------Boleto-------\n'
        origin = "ORIGEN:\t"
        destiny = "DESTINO:\t"
        result = ticket + origin + string1 + "\n" + destiny + string2
        print(result)
        return result
    

                
    def __init__(self, dictionary):
        """Data base constructor.
        Args:
            dictionary: dataset dictionary.
        """
        self.data = dictionary
