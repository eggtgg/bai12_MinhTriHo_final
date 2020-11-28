import random
import numpy as np
import string
first_string= string.ascii_uppercase
next_string= string.ascii_lowercase
n=random.randrange(50,101)
list_dict=list(np.zeros(n))
print((list_dict))
def name_one():
    length_name = random.randrange(1, 15)
    k= random.choice(first_string)
    for i in range(length_name):
        k+= random.choice(next_string)
    return k
def age():
    rd_age= random.randrange(0,101)
    return rd_age
for i in range(len(list_dict)):
    list_dict[i]= dictionary = {'name': name_one(), 'age': age()}
print(list_dict)


