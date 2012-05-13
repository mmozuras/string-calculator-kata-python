from calculator import add

def describe_string_calculator():
  def returns_0_for_empty_string():
    assert add('') == 0

  def returns_bare_numbers():
    assert add('0') == 0
    assert add('1') == 1

  def adds_numbers():
    assert add('1,2') == 3
    assert add('1,10') == 11

  def describe_delimiters():
    def can_be_newlines():
      assert add('1\n2') == 3
