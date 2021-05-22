from leap_year import leap_year_test as lp

class Test_time:	
	
	def test_wc_correct(self): 
		assert lp(2000) == True
		assert lp(1999) == False
		assert lp(4) == True
		
	def test_wc_type(self): 
		assert lp(" ` ") == False
		assert lp("Hello") == False
		assert lp("2000") != False
 
	def test_wc_null(self): 
		assert lp(-1) == False
		assert lp(" ") == False
		assert lp(0) == False