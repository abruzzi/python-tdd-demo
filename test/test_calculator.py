import unittest

from app.calculator import Calculator

class CalculatorTest(unittest.TestCase):

	def setUp(self):
		self.calc = Calculator()

	def test_should_return_3_when_add_1_and_2(self):
		ret = self.calc.add(1, 2)
		self.assertEqual(3, ret)

	def test_should_throw_exception_when_no_numbers_passes(self):
		self.assertRaises(ValueError, self.calc.add, "1", 2)

	def test_should_return_1_when_sub_3_and_2(self):
		ret = self.calc.sub(3, 2)
		self.assertEqual(1, ret)

if __name__ == "__main__":
	unittest.main()