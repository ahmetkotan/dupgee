try:
    import socket
except Exception as import_error:
    print(str(import_error))
    import usocket as socket

from .parsers import parse_http_request
from .matcher import find_view


def run_server(port=8080):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("", port))
    sock.listen(1)

    while True:
        connection, addr = sock.accept()
        data = connection.recv(4096).decode()
        try:
            request = parse_http_request(data=data, ip_address=addr[0], connection=connection)
            response = find_view(request=request)
        except Exception as connection_error:
            print(str(connection_error))
            connection.close()
            continue

        connection.send("HTTP/1.1 {0}\n".format(response.get_status_code()))
        connection.send("Content-Type: {0}\n".format(response.get_content_type()))
        connection.send("Connection: close\n\n")
        connection.sendall(response.get_content())
        connection.close()
