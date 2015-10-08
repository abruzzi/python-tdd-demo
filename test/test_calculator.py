import unittest

from app.calculator import Calculator

class CalculatorTest(unittest.TestCase):

	def test_should_return_3_when_add_1_and_2(self):
		calc = Calculator()
		ret = calc.add(1, 2)
		self.assertEqual(ret, 3)

	def test_should_throw_exception_when_no_numbers_passes(self):
		calc = Calculator()
		self.assertRaises(ValueError, calc.add, "1", 2)
		
if __name__ == "__main__":
	unittest.main()