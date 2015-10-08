class Calculator:
	def add(self, a, b):
		if isinstance(a, int) and isinstance(b, int):
			return a + b
		else:
			raise ValueError

	def sub(self, a, b):
		return a - b