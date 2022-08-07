#day2
from __future__ import division
from math import pi


first_name='Kartik'
last_name='Kapoor'
full_name='Kartik Kapoor'
country='India'
city='New Delhi'
age=20
year=2022
is_married=False
is_true=True
is_light_on=True
first_name,last_name,age,country,city='Kartik','Kapoor',20,'India','New Delhi'
print(type(first_name))
print(type(age))
print(type(is_married))
print(len(first_name))
print(max(len(first_name),len(last_name)))
num_one,num_two=5,4
total=num_one+num_two
diff=num_two-num_one
product=num_one*num_two
division=num_one/num_two
remainder=num_two%num_one
exp=num_one**num_two
floor_division=num_one//num_two
print(num_one,num_two,total,diff,product,division,remainder,exp,floor_division)
rad=input('Enter Radius of circle:')
radius=float(rad)
area_of_circle=pi*radius*radius
circum_of_circle=2*pi*radius
print(area_of_circle,circum_of_circle)
help('keywords')