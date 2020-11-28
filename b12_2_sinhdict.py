import random, string
a = string.ascii_lowercase
first_string= string.ascii_uppercase
k=random.choice(first_string)
n=random.randrange(2,15)
age=random.randrange(1,100)
for i in range(n):
	k=k+random.choice(a)
dictionary={'name':k,'age':age}
print(dictionary)