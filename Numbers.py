# Common Number Operations Library

class Numbers:
    """
        Class is for number operations
    """
    
    def is_even(self, x):
        """
        Checks if a number is even. (Sphinx style documentation)

        :type x: int
        :param x: number to check
        :return: `True` if number is even, `False` otherwise
        :rtype: bool
        """
        return x%2 == 0

    def add(self, *args):
        """
        Adds numbers passed in args.

        :type args: float
        :param args: numbers to add
        :return: Sum of numbers passed as args
        :rtype: float
        """
        sum = 0
        for arg in args:
            sum += float(arg)
        return sum
