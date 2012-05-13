def add(string):
  if string.startswith('-'):
    raise ValueError
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
    delimiter_spec, string = string.split('\n', 1)
    delimiter = delimiter_spec[2:]
    string = string.replace(delimiter, ',')
  return string

def _add_numbers_in_string(string):
  return sum(map(int, string.split(',')))
