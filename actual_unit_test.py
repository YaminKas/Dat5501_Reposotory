import unittest
from unit_testing_activity import run,addition



class testing_cases(unittest.TestCase):
    def test_add(self):

        self.assertEqual(addition(2,3),5)

        self.assertEqual(addition(-6,3),-3)

        self.assertEqual(addition(3.1,5.4), 8.5)

if __name__ == "__main__":
    unittest.main()




