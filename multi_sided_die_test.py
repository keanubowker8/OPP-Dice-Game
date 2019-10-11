from multi_sided_die import *

md = MultiSidedDie(6)

def test_roll():
	md.roll()
	assert md.value == 1

def test_get_value():
	assert md.get_value() == 1

def test_set_value():
	md.set_value(8)
	assert md.value == 8	

