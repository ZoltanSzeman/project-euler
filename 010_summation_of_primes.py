from math import sqrt

primes = [2,3]
num = primes[1]
while num < 2000000:
  num += 2
  div_list = list(range(2,int(sqrt(num))+1))
  for div in div_list:
    if num % div == 0:
      break
  else:
    primes.append(num)
if primes[-1] > 2000000:
  print(sum(primes[:-1]))
  print(primes[-2])
else:
  print(sum(primes))
  print(primes[-1])
  print(True)
