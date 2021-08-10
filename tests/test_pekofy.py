from src import pekofy
import unittest

class TestPeko(unittest.TestCase):
    def test_with_input(self):
        puncs = ['.', '!', '?', '. ', '! ', '? ', ' ']
        for i in puncs:
            self.assertEqual(pekofy.pekofy('hello world' + i), 
                            'hello world {}{}'.format('peko', i))

if __name__ == '__main__':
    unittest.main()

'''
class TestSample(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1,1); <---- bruh XDDDDDD
'''
