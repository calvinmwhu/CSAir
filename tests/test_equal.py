__author__ = 'calvinmwhu'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        dic1 = {'a':1,'b':2}
        dic2 = {'a':1,'b':2}

        print(id(dic1), id(dic2))

        self.assertEqual(dic1,dic2)

        print(dic1 is dic2)

        a = 'hello'

        b=a
        c=a[:]
        print(b is a)
        print(c is a)


if __name__ == '__main__':
    unittest.main()
