"""Module docstring."""


def build_route(path: str=None):
    """Function docstring."""
    home = f'/'
    if path:
        return f'{home}{path}'
    return home
