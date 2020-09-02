from math import sqrt
num = 3
n = 3
count = 0
while count*2 < 500:
  count = 0
  num += n
  for x in range(1,int(sqrt(num))):
    if num % x == 0:
      count += 1
  n += 1
print(num)
