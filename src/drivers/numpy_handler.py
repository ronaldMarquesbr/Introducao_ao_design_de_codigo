import numpy
from typing import List


class NumpyHandler:
    def __init__(self):
        self.__np = numpy

    def standard_deviation(self, numbers: List[float]) -> numpy.floating:
        return self.__np.std(numbers)
