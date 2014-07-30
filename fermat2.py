def fermat(a,b,c,n):
  if n <= 2:
    print "n must be greater than 2"
    return
  if a == b or a == c or b == c:
    print "a b and c must be unique integers"
    return
  if a**n + b**n == c**n:
    print "Holy smokes, Fermat was wrong!"
  else:
    print 'No, that doesnt work'
    return
def check_fermat():
  a = raw_input('a = ?\n')
  a = int(a)
  b = raw_input('b = ?\n')
  b = int(b)
  c = raw_input('c = ?\n')
  c = int(c)
  n = raw_input('n = ?\n')
  n = int(n)
  fermat(a, b, c, n)

