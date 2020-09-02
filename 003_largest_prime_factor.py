n = 600851475143
div = list(range(3,1000000,2))
for d in div[::-1]:
  if n % d == 0:
    prime_check = list(range(2,d))
    for p in prime_check:
      if d % p == 0:
        break
    else:
      print(d)
