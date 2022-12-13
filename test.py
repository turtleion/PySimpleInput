import unittest
# TEST - EPL/ROL/RPL 1.0

import PySimpleInput
class TestSum(unittest.TestCase):
    def test_pysimpleinput_class(self):
        self.assertEqual(PySimpleInput.test(), True)


if __name__ == "__main__":
    unittest.main()
