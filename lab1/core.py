import pandas
import logging


class Core(object):

    def __init__(self, file):

        self.__data = pandas.read_csv(file, sep=',')
        print(f'dataframe = {self.__data}')
