import unittest

class Submarino(object):
    pass

class SubmarinoTest(unittest.TestCase):

    def testFoo(self):
        sub = Submarino()
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()