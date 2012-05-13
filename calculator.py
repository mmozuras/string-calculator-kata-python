def add(string):
  if string:
    return _add_numbers_in_string(string)
  else:
    return 0

def _add_numbers_in_string(string):
  return sum(map(int, string.split(',')))
