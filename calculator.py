def add(string):
  string = _normalize_delimiters(string)
  if string:
    return _add_numbers_in_string(string)
  else:
    return 0

def _normalize_delimiters(string):
  string = _normalize_custom_delimiter(string)
  string = string.replace('\n', ',')
  return string

def _normalize_custom_delimiter(string):
  if string.startswith('//'):
    delimiter = string[2]
    string = string[4:]
    string = string.replace(delimiter, ',')
  return string

def _add_numbers_in_string(string):
  return sum(map(int, string.split(',')))
