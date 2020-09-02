def path(plist,clist):
  count = 1
  while count != 21:
    clist.append(plist[count] + clist[count-1])
    count += 1
  return clist

lattice = ['#',[1] * 21,[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
count = 2
while count != 21:
  lattice[count] = path(lattice[count-1],lattice[count])
  count += 1
print(sum(lattice[20]))
'''list2 = [1]
list3 = [1]
list4 = [1]
list5 = [1]
list6 = [1]
list7 = [1]
list8 = [1]
list9 = [1]
list10 = [1]
count = 1
while count != 20:
  list2.append(list1[count] + list2[count-1])
  count += 1
count = 1
while count != 20:
  list3.append(list2[count] + list3[count-1])
  count += 1
count = 1
while count != 20:
  list4.append(list3[count] + list4[count-1])
  count += 1
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)
print(list10)'''
