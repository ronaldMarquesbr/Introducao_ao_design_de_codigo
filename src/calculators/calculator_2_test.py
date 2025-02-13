from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_interface_handler import DriverInterfaceHandler


class MockRequest:
    def __init__(self, body) -> None:
        self.json = body


class MockDriverHandler(DriverInterfaceHandler):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3


def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})

    calculator_2 = Calculator2(MockDriverHandler())
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, Dict)
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.33}}
