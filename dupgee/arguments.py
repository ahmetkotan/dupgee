from dupgee.create import create_project
from dupgee.helper import help_ginger

try:
    import sys
except Exception as e:
    print(str(e))
    import usys as sys

options = {
    "create": {"method": create_project, "kwargs": {"name": True}},
    "help": {"method": help_ginger, "kwargs": {}}
}


def check_option(arguments):
    option_name = arguments[1]
    other_options = arguments[2:]

    option = options.get(option_name, None)
    if option:
        kwargs = {}
        for opt, keyword in zip(other_options, option.get("kwargs").keys()):
            kwargs[keyword] = opt

        required_options = [k for k, v in option.get("kwargs").items() if v]
        if frozenset(kwargs.keys()) != frozenset(required_options):
            return None, None

        return option.get("method"), kwargs

    return None, None


def parse_arguments(arguments):
    if len(arguments) == 1:
        help_ginger()
        sys.exit(1)

    method, kwargs = check_option(arguments=arguments)
    if method is None:
        help_ginger()
        sys.exit(1)

    return method, kwargs



