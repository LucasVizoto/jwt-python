class HttpResponse:
    def __init__(self, body: dict, status_code: int) -> None:
        self.bode = body
        self.status_code = status_code