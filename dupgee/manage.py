import sys

from dupgee.arguments import parse_arguments


def execute():
    method, kwargs = parse_arguments(arguments=sys.argv)
    method(**kwargs)

