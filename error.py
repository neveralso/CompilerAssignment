# encoding: utf-8


class IEError(Exception):
    def __init_(self, msg):
        self.args = msg