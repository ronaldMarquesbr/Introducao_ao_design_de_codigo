from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_interface_handler import DriverInterfaceHandler
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator2:
    def __init__(self, driver_handler: DriverInterfaceHandler) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        formatted_response = self.__format_response(calculated_number)

        return formatted_response

    @staticmethod
    def __validate_body(body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_deviation(first_process_result)

        return 1 / result

    @staticmethod
    def __format_response(calculated_number: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calculated_number, 2)
            }
        }
