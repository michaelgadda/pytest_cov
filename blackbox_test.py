import unittest 
from leap_year import leap_year_test as lp



class TestPalindrome(unittest.TestCase):
    
    def test_corrrectness(self):
        self.assertEqual(lp(2000), True)
        self.assertEqual(lp(1999), False)
        self.assertEqual(lp(0), False)
   
    def test_type(self):
        self.assertEqual(lp("!"), False)
        self.assertEqual(lp(" ```"), False)
        self.assertNotEqual(lp(2000), False)
        self.assertNotEqual(lp(4), False)

    def test_null(self): 
        self.assertEqual(lp("-1"), False)
        self.assertEqual(lp(" "), False)
        self.assertEqual(lp("  "), False)
        self.assertNotEqual(lp("  "), False)

if __name__ == '__main__': 
	unittest.main()
