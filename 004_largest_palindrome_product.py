import os
os.system('cls')

n3a_list = list(range(100,1000))
n3b_list = list(range(100,1000))
n = 999999
n_div = []
count = 1
while count != 900:
  for n3a in n3a_list[::-1]:
    if n % n3a == 0:
      #print('n3a:',n3a)
      for n3b in n3b_list[::-1]:
        if (n / n3a) / n3b == 1:
          n_div.append(n)
          break
  if count % 100 == 0:
    n = n - 11
  elif count % 10 == 0:
    n = n - 110
  else:
    n = n - 1100
  count += 1
print(max(n_div))
