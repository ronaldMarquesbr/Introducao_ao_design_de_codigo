from typing import Dict
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_interface_handler import DriverInterfaceHandler


class Calculator3:
    def __init__(self, driver_handler: DriverInterfaceHandler) -> None:
        self.driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        pass
