from model.csvReader import CsvReader
from model.database import DataBase
import threading
        
def main():
    compute()
    
def compute():
    """Save the route of each datasets, creates an object
    to read csv files that return a dictionary of the datasets.
    Creates a data base for each dictionary and creates two threads
    to manage each requests of the data bases while printing its results.
    """
    dataset1 = 'project/data/dataset1.csv'
    dataset2 = "project/data/dataset2.csv"

    reader = CsvReader()

    data1 = reader.readCsv(dataset1)
    data2 = reader.readCsv(dataset2)

    database1 = DataBase(data1)
    database2 = DataBase(data2)

    Thread1 = threading.Thread(target=database1.fill, args= (1, ))
    Thread2 = threading.Thread(target=database2.fill, args= (2, ))


    Thread1.start()
    Thread2.start()


if __name__ == "__main__":
    main()