def add(string):
  if ',' in string:
    return sum(map(int, string.split(',')))
  return int(string) if string else 0
