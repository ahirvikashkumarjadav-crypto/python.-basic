#numeric data types
x=10
y=3.14
z=3+2j

print(type(x))
print(type(y))
print(type(z))

#arithmetic operation
a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

x=10; y=3

#comparison
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)

#logical operators

print(x<15 and y>15)
print(x<15 or Y<15)
print(not(x==y))

#rounding modules

import math
x=10; y=3
#ceil()
print(math.ceil(4.2))
print(math.ceil(4.8))
print(math.floor(4.2))
print(math.floor(4.8))

print(round(4.2))
print(round(4.8))

#number 
number=[10,20,30]
#strings
names=['msaurav,'"bikash", "ayush"]
#booleean
satus=[True,False,True]
#mixed data

data=["saurav",17,True]
print(data)
print(data[1])


#LIST OPERATION
names=["saurav","ayush","bikash",]
print("originallist:",names)
names.append("saurav")
print("after append('saurav'):",names)
names.remove("saurav")
print("after remove('ayush'):",names)
removed_name=names.pop(1)
print("removed using pop(1):",removed_name)
print("list after pop():",names)
print("length of list:",len(names))

#name is now['saurav', bikash']
print("is 'saurav 'present?","saurav "in names )
print("is'bikash' present?","saurav in names")
names.append("zoya")
names.append("singh")
print("before sorting ",names)
names.sort()
print("after sorting:",names)
names.reverse()

