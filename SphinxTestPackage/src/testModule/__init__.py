"""
testModule
----------------------
This is a Module which has Class for Sphinx Testing
"""


class Sphinxx(object):
    """Class which is responsile for testing Sphinx """

    def __init__(self, connection_string):
        """
        This is a string which will be printed as output
        :param connection_string: str
        """
        print(connection_string)
        self.connection_string = connection_string

    def add_num(self, a, b):
        """
        This function returns sum of two numbers
        :param a: First num
        :param b: Second num
        :return: Sum of numbers
        """
        print("Sum calculated successfully")
        return a+b
