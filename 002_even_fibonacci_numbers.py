fibonacci = [1,2]
count = 2
while fibonacci[count-1] < 4000000:
  fibonacci.append(fibonacci[count-2]+fibonacci[count-1])
  count += 1
fibonacci.pop()
fibonacci_even = [x for x in fibonacci if x % 2 == 0]
#print(fibonacci)
print(sum(fibonacci_even))
