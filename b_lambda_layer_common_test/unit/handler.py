import pytest


def handler(*args, **kwargs):
    """
    Programmatic access to run tests with pytest.

    WARNING. Do not delete this file. It is also used for lambda functions to run unit tests.
    """
    return dict(ExitCode=pytest.main([]))
