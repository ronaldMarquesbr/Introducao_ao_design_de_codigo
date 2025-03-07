class HttpUnprocessableEntity(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.name = "Unprocessable Entity"
        self.message = message
        self.status_code = 422
