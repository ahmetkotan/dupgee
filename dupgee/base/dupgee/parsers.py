from .request import HttpRequest
import json


def parse_data_block(data_string, headers):
    request_data = {}
    content_type = headers.get("Content-Type", None)

    if content_type == "application/json":
        return json.loads(data_string)
    elif content_type == "application/x-www-form-urlencoded":
        if data_string.startswith("{"):
            return json.loads(data_string)
        for string in data_string.split("&"):
            data_key, data_value = string.split("=", 1)
            request_data[data_key.strip()] = data_value.strip()

    return request_data


def parse_url_parameters(absolute_path):
    parameters = {}
    if "?" in absolute_path:
        absolute_path, parameter_string = absolute_path.split("?")
        if parameter_string:
            parameters = {
                p.split("=")[0]: p.split("=")[1]
                for p in parameter_string.split("&")
            }

    return absolute_path, parameters


def wait_data_block(connection, data_lines, headers):
    content_length = headers.get("Content-Length", None)
    if content_length:
        if content_length.isdigit():
            content_length = int(content_length)
            data_length = len("\n".join(data_lines))
            while data_length < content_length:
                data = connection.recv(4096).decode()
                data_lines.extend(data.split("\n"))
                data_length = len("\n".join(data_lines))

            return "\n".join(data_lines)

    return "\n".join(data_lines)


def parse_http_request(connection, data, ip_address):
    request_header = data.split("\n")
    method, absolute_path, http_version = request_header[0].strip().split()

    headers = {}
    data_block = False
    data_lines = []

    for i in request_header[1:]:
        if i == "\r":
            data_block = True
            continue
        if i:
            if data_block:
                data_lines.append(i)
            else:
                i = i.strip()
                header_key, header_value = i.split(":", 1)
                headers[header_key.strip()] = header_value.strip()

    data_string = wait_data_block(connection=connection, data_lines=data_lines, headers=headers)
    request_data = parse_data_block(data_string=data_string, headers=headers)
    absolute_path, parameters = parse_url_parameters(absolute_path=absolute_path)

    print(ip_address, method, absolute_path, len(data_string))
    return HttpRequest(
        method=method,
        path=absolute_path,
        headers=headers,
        parameters=parameters,
        ip_address=ip_address,
        data=request_data,
    )

