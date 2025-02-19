import numpy
from src.drivers.interfaces.driver_interface_handler import DriverInterfaceHandler
from typing import List


class NumpyHandler(DriverInterfaceHandler):
    def __init__(self):
        self.__np = numpy

    def standard_deviation(self, numbers: List[float]) -> numpy.floating:
        return self.__np.std(numbers)

    def variance(self, numbers: List[float]) -> numpy.floating:
        return self.__np.var(numbers)
