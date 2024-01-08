import os


class Service:

    def __init__(self) -> None:
        self._method = None
        self._path = None
        self._handler_file = None
        self._cors = []

    def set_method(self, method: str):
        if method not in ['GET', 'POST', 'PUT', 'DELETE']:
            raise Exception('Invalid method')
        self._method = method

    def set_path(self, path: str):
        if path[0] != '/':
            raise Exception('Please start with /')
        self._path = path

    def set_handler_file(self, handler_file: str):
        if not os.path.exists(handler_file):
            raise Exception('File not found')
        self._handler_file = handler_file

    def cors_allow_origins(self, origins: list):
        self._cors.append({
            'allowed_origins': origins
        })

    def get_resource(self):
        if not self._method:
            raise Exception('Method not set')
        if not self._path:
            raise Exception('Path not set')
        if not self._handler_file:
            raise Exception('Handler file not set')
        if not self._cors:
            raise Exception('CORS not set')
        return {
            'method': self._method,
            'path': self._path,
            'handler_file': self._handler_file,
            'cors': self._cors
        }
