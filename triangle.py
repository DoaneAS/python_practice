mn
def triangle(a, b, c):
  if a > b + c or b > a + c or c > b + a:
      print 'no'
  else:
    print 'yes'
    
def is_triangle():
  a = raw_input('a = ?\n')
  a = int(a)
  b = raw_input('b = ?\n')
  b = int(b)
  c = raw_input('c = ?\n')
  c = int(c)
  triangle(a, b, c)
