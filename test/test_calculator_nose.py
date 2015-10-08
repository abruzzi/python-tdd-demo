from nose.tools import *

from app.calculator import Calculator

calc = None

def setup():
	global calc
	calc = Calculator()

@with_setup(setup, None)
def test_should_return_3_when_add_1_and_2():
	ret = calc.add(1, 2)
	assert 3 == ret

@raises(ValueError)
@with_setup(setup, None)
def test_should_throw_exception_when_no_numbers_passes():
	calc.add("1", 2)

@with_setup(setup, None)
def test_should_return_1_when_sub_3_and_2():
	ret = calc.sub(3, 2)
	assert 1 == ret