import unittest
from plus import plus
 

class TestPlus(unittest.TestCase):
    def test_plus(self):
        actual_result = plus(1, 1)
    
        self.assertEqual(actual_result, 2)

if __name__ == '__main__':
    unittest.main()