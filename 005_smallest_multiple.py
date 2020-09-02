n = 2520
div_list = list(range(1,21))
while True:
  div_count = 0
  for div in div_list[::-1]:
    if n % div == 0:
      div_count += 1
    else:
      break
  if div_count == 20:
    break
  n += 20
print(n)
