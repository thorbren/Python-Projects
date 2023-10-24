alist = ['accounting', 3.5, 'finance', 100]
print("OG list is: ", alist)
alist[0] = 'business'
print("new list: ", alist)
alist[-1] = 6
print("new new list: ", alist)

blist = [100, 'zoo', 20]
clist = alist + blist
print("combine list: ", clist)


print(alist * 2)

length = len(alist)
print(length)

alist = ['accounting', 'finance', 'marketing']
alist1= alist[1:4]
print(alist[1:4])
print(alist[0:-1])
print(alist[:2])
print(alist[1:])
print(alist[0:2:1])


dlist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("The original list is ", dlist)
index = int(input("Enter a number between 0 and 11: "))
print(f"The substring of the list between 0 and {index} is: ", dlist[0:index])
print(f"The substring of the list between the end of the list and {index} is: ", dlist[-index:])

index2 = int(input("Enter a number for the first position in the list: "))
index3 = int(input("Enter a number for the second position in the list: "))
dlist[index2], dlist[index3] = dlist[index3], dlist[index2]
# or you can make 2 temporary variables and assign them (see below)
# temp1 = dlist[index2]
# temp2 = dlist[index3]
# dlist[index2] = temp2
# dlist[index3] = temp1
print("New list is ", dlist)


print(alist)
alist.append("marketing")
print(alist)

import random

alist2 = []
num = int(input("Enter a number of elements: "))
for i in range(num):
    number = random.randint(1, 500)
    alist2.append(number)
print(alist2)


listy = ['shore', 'shell', 'sea', 'wave']
item = listy.pop(1)
print(listy)

del(listy[1])
print(listy)