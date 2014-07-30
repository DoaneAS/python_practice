def fermat(a,b,c,n):
  if n <= 2:
    print "n must be greater than 2"
    return
  if a == b OR a == c or b == c:
    print "a b and c must be unique integers"
    return
  if a**n + b**n == c**n:
    print "Holy smokes, Fermat was wrong!"
  else:
    print 'No, that doesnt work'
    return