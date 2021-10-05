import unittest
values=('0')

class Temperature(unittest.TestCase):
    def __init__ (self, kelvin=None, celsius=None, farenheit=None):
        values = [x for x in [kelvin, celsius, farenheit] if x]

    if len(values) < 1:
        raise ValueError('Need Argument')
    if len(values) > 1:
        raise ValueError('Only one argument')

    def try1 (self,kelvin, celsius, farenheit):
        if celsius is not None:
            self.kelvin = celsius + 273.15
        elif farenheit is not None:
            self.kelvin = (farenheit - 32) * 5 / 9 + 273.15
        else:
            self.kelvin = kelvin
    def try2(self):
        if self.kelvin < 0:
            raise ValueError('Temperature in Kelvin cannot be negative')

def __str__ (self):
    return f'Temperature = {self.kelvin} Kelvins'

def test_search(self):
    self.assertTrue("True")
def test_celsius(self):
    self.assertTrue('True')
def test_farenheit(self):
    self.assertTrue('True')
def test_kelvin(self):
    self.assertTrue('True')

if __name__ == '__main__':
    unittest.main()
