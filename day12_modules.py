import mymodule
print(mymodule.generate_fulll_name('Kartik','Kapoor'))

from mymodule import generate_fulll_name as fullname,sum_two_nums as total,person as p,gravity as g
print(fullname('Kartik','Kapoor'))
print(total(1,2))
mass=100
print(mass*g)
print(p['firstname'])

import os
#os.mkdir('Hello World') #create directory
#os.chdir('Dattebayo') #change current directory
os.getcwd() #get current work directory
#os.rmdir('') #remove directory

from statistics import * #import all 
ages=[20,20,4,24,25,22,26,20,23,22,26]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

import math
print(math.pi)
print(math.sqrt(2))
print(math.pow(2,3))
print(math.floor(9.81))
print(math.ceil(9.81))
print(math.log10(100))

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

import random
print(random.randint(5,20))
print(random.random())

def random_user_id():
    return ''.join(random.choice(string.ascii_letters+string.digits)for x in range(6))
print(random_user_id())

def user_id_gen_by_user():
    ch=input('Enter number of characters\n')
    no=input('Enter number of IDs\n')
    for i in range(int(no)):
        print(''.join(random.choice(string.ascii_letters+string.digits)for x in range(int(ch))))
user_id_gen_by_user()

def rgb_color_gen():
    col1=random.randint(0,255)
    col2=random.randint(0,255)
    col3=random.randint(0,255)
    return 'rgb({},{},{})'.format(col1,col2,col3)
print(rgb_color_gen())

def list_of_hexa_colors():
    hex=list()
    n=random.randint(0,9)
    for i in range(n):
        hex.append('#'+''.join(random.choice('a'+'b'+'c'+'d'+'e'+'f'+string.digits)for x in range(6)))
    return hex
print(list_of_hexa_colors())

def list_of_rgb_colors():
    n=random.randint(0,9)
    arr=list()
    for i in range(n):
        col1=random.randint(0,255)
        col2=random.randint(0,255)
        col3=random.randint(0,255)
        arr.append('rgb({},{},{})'.format(col1,col2,col3))
    return arr
print(list_of_rgb_colors())

def generate_colors(format,n):
    arr=list()
    if format=='hexa':
        for i in range(n):
            arr.append('#'+''.join(random.choice('a'+'b'+'c'+'d'+'e'+'f'+string.digits)for x in range(6)))
    elif format=='rgb':
        for i in range(n):
            col1=random.randint(0,255)
            col2=random.randint(0,255)
            col3=random.randint(0,255)
            arr.append('rgb({},{},{})'.format(col1,col2,col3))
    return arr
print(generate_colors('hexa',3))

def shuffle_list(arr):
    random.shuffle(arr)
    return arr
print(shuffle_list([1,2,3,4,5]))

def rand_arr():
    arr=list()
    while len(arr)<7:
        val=random.randint(0,9)
        if val not in arr:
            arr.append(val)
    return arr
print(rand_arr())