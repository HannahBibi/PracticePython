class MethodNotImplementedException(Exception):
    def __init__(self, message):
        self._message = message
