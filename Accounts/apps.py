from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'Accounts'

    def ready(self):
        import Accounts.signals


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


class ClassName(object):
    """docstring for ClassName"""

    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg


def function():
    re
