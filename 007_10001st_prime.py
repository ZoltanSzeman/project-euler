from math import sqrt

primes = [2,3]
count = 2
num = primes[1]
while count != 10001:
  num += 2
  div_list = list(range(2,int(sqrt(num))+1))
  for div in div_list:
    if num % div == 0:
      break
  else:
    primes.append(num)
    count += 1
print(primes[10000])
