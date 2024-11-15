import os
import unittest

from src.add import add


class MyTestCase(unittest.TestCase):
    def test_add(self):
        # print process id
        print("Process id: ", os.getpid())

        self.assertEqual(add(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
