"""Module docstring."""
import sys
from getopt import getopt, GetoptError
from waitress import serve
from rng.web.app import app


def print_help(exit_code=None):
    """Function docstring."""
    path = sys.argv[0]
    idx = path.rfind('/')
    if idx >= 0:
        path = path[idx+1:]
    print(f'Usage: python3 {path} [-h|--help] [-p|--port <port_number>]')

    if exit_code is not None:
        sys.exit(exit_code)

def main(argv):
    """Function docstring."""
    port = 8080

    try:
        opts, _ = getopt(argv, 'hp:', ['help', 'port='])
    except GetoptError:
        print_help(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print_help(0)
        elif opt in ('-p', '--port'):
            try:
                port = int(arg)
            except ValueError:
                print(f'Error: "{arg}" is not a valid port number')
                sys.exit(2)

    serve(app, host='0.0.0.0', port=port)

if __name__ == '__main__':
    main(sys.argv[1:])
