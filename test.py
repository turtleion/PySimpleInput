import unittest
# TEST - EPL/ROL/RPL 1.0

from PySimpleInput import test
class TestSum(unittest.TestCase):
    def test_pysimpleinput_class(self):
        self.assertEqual(test(), True)


if __name__ == "__main__":
    unittest.main()
