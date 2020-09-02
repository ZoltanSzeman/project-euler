chain = 0
for num in range(2,1000000):
  count = 1
  x = num
  while x != 1:
    if x % 2 == 0:
      x = x/2
    else:
      x = x*3 + 1
    count += 1
  if chain < count:
    chain = count
    chain_no = num
print(chain,chain_no)
