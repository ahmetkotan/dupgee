class HttpRequest:
    method = ""
    path = ""
    headers = {}
    parameters = {}
    ip_address = ""
    data = {}

    def __init__(self, method, path, headers, parameters, ip_address, data=None):
        self.method = method
        self.path = path
        self.headers = headers
        self.parameters = parameters
        self.ip_address = ip_address
        self.data = data or {}
