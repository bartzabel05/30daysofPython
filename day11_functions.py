from __future__ import print_function
from audioop import reverse
from math import pi
from random import randrange
from re import M


def add_two_numbers(a,b):
    return a+b;

s=add_two_numbers(2,3)
print(s)

def area_of_circle(r):
    return pi*r*r;
area=area_of_circle(7)
print(area);

def add_all_nums(*args):
    total=0
    for arg in args:
        if(type(arg)==int):
            total+=arg
        else:
            print("Not an integer")
    return total
sums=add_all_nums(2,3,'5')
print(sums)

def convert_celsius_to_fahrenheit(c):
    f=c*(9/5)+32
    return f
print(convert_celsius_to_fahrenheit(38))

def check_season(month):
    if month=='April' or month=='June' or month=='May':
        return 'Summer'
    elif month=='July' or month=='August' or month=='September':
        return 'Monsoon'
    elif month=='October' or month=='November':
        return 'Autumn'
    elif month=='December' or month=='January' or month=='February':
        return 'Winter'
    else:
        return 'Invalid Season'
print(check_season('May'))

def calculate_slope(x1,y1,x2,y2):
    if x2-x1!=0:
        m=(y2-y1)/(x2-x1)
    else:
        print('cant caclulate slope')
        return 0
    return m
print(calculate_slope(2,3,5,4))

def solve_quadratic_eqn(a,b,c):
    if a!=0 and b*b-4*a*c>0:
        sol1=((-b)+((b*b)-(4*a*c))**(1/2))/(2*a)
        sol2=((-b)-((b*b)-(4*a*c))**(1/2))/(2*a)
        print(sol1,sol2)
    elif a!=0 and b*b-4*a*c==0:
        sol1=sol2=((-b)+((b*b)-(4*a*c))**(1/2))/(2*a)
        print(sol1,sol2)
    elif a!=0 and b*b-4*a*c<0:
        print('imaginary solution')
        sol1=((-b)+((b*b)-(4*a*c))**(1/2))/(2*a)
        sol2=((-b)-((b*b)-(4*a*c))**(1/2))/(2*a)
        print(sol1,sol2)
    else:
        print('Not quadratic eqn')
solve_quadratic_eqn(1,2,3)

def print_list(ls):
    for l in ls:
        print(l,end=" ")
print_list([1,2,3,4,5])
print('\n')

def reverse_list(ls):
    end=len(ls)-1
    rev_ls=list()
    for i in range(end,-1,-1):
        rev_ls.append(ls[i])
    return rev_ls
print(reverse_list([1,2,3,4,5]))
print(reverse_list(['A','B','C']))

def capitalize_list_items(ls):
    end=len(ls)
    cap_ls=list()
    for i in range(0,end,1):
        cap_ls.append(ls[i].upper())
    return cap_ls
print(capitalize_list_items(['a','b','c','d']))

def add_item(staff,food):
    staff.append(food)
    return staff
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff,'Meat'))

def remove_item(ls,it):
    ls.remove(it)
    return ls
print(remove_item(food_staff,'Mango'))

def sum_of_numbers(r):
    total=0
    for i in range(r+1):
        total+=i
    return total
print(sum_of_numbers(5))

def sum_of_evens(r):
    totale=0
    for i in range(r+1):
        if i%2==0:
            totale+=i
    return totale
print(sum_of_evens(5))

def sum_of_odds(r):
    total=0
    for i in range(r+1):
        if i%2!=0:
            total+=i
    return total
print(sum_of_odds(5))

def evens_and_odds(n):
    counto,counte=0,0
    for i in range(n+1):
        if i%2!=0:
            counto+=1
        elif i%2==0:
            counte+=1
    return counte,counto
print('Evens and odds',evens_and_odds(100))

def factorial(num):
    fac=1
    if num<0:
        print('No factorial')
    elif num==0:
        return fac
    else:
        for i in range(1,num+1):
            fac=fac*i
    return fac
print(factorial(5))

def is_empty(param):
    if len(param)==0:
        print('Empty')
    else:
        print('Not empty')
is_empty([1])

def calculate_mean(ls):
    end=len(ls)
    total=0
    for l in ls:
        total+=l
    return total/end

def calculate_median(ls):
    end=len(ls)-1
    if end%2==0:
        mid=end/2
        return ls[int(mid)]
    else:
        mid1=end/2
        mid2=mid1+1
        return (ls[int(mid1)]+ls[int(mid2)])/2

print('Mean',calculate_mean([1,2,3,4,5]))
print('Median',calculate_median([1,5,7,8,9,6]))

