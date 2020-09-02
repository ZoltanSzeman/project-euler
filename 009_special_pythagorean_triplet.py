from math import sqrt

a_max = 333
b_max = 500
a_list = list(range(1,a_max))
b_list = list(range(1,b_max))
c_list = list(range(1,int(sqrt(a_max**2+b_max**2))))
for a in a_list:
  for b in b_list:
    if b > a:
      for c in c_list:
        if c > b:
          if (a**2 + b**2) == c**2 and a + b + c == 1000:
            print(a,b,c)
            print(a * b * c)
