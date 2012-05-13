from calculator import add

def describe_string_calculator():
  def returns_0_for_empty_string():
    assert add('') == 0

  def returns_bare_numbers():
    assert add('1') == 1
