import unittest
from plus import plus
 

# class TestPlus(unittest.TestCase):
#     def test_plus(self):
#         actual_result = plus(1, 1)
    
#         self.assertEqual(actual_result, 2)


# テストコード
# class TestPlus():
def test_add():
    res = plus(1, 2)
    assert res == 3    

if __name__ == '__main__':
    test_add()