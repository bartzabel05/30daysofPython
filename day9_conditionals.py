age=input('Enter your age:')
if int(age)>=18:
    print('You are old enough to drive')
else:
    print('You need {} more years to learn to drive'.format(18-int(age)))

my_age=20
your_age=input("Enter your age:")
if my_age>int(your_age):
    print('Im {} years older than you'.format(my_age-int(your_age)))
elif my_age<int(your_age):
    print('You are {} years older than me'.format(int(your_age)-my_age))
else:
    print('We are of the same age') 

a=input('Enter number one:')
b=input('Enter number two:')
if int(a)>int(b):
    print('{} is greater than {}'.format(a,b))
elif int(a)<int(b):
    print('{} is greater than {}'.format(b,a))
else:
    print('{} is equal to {}'.format(a,b))   

marks=int(input("Enter marks here:"))
if marks>=90 and marks<=100:
    grade='A'
elif marks>=70 and marks<90:
    grade='B'
elif marks>=60 and marks<70:
    grade='C'
elif marks>=50 and marks<60:
    grade='D'
else:
    grade='F'
print('Your grade is {}'.format(grade))

mth=str(input("Enter month:"))
if mth=="September" or mth=="October" or mth=="November":
    season="Autumn"
elif mth=="December" or mth=="January" or mth=="February":
    season="Winter"
elif mth=="March" or mth=="April" or mth=="May":
    season="Spring"
else:
    season="Summer"
print("Season is {}".format(season))

fruit=str(input("Enter fruit:"))
fruits = ['banana', 'orange', 'mango', 'lemon']
if fruit in fruits:
    print('{} already exists in the list'.format(fruit))
else:
    fruits.append(fruit)
print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
mid=(len(person['skills'])-1)/2
if 'skills' in person:
    if 'Python' in person['skills']:
        print('Person skilled in Python')
    else:
        print('Person skilled in {}'.format(person['skills'][int(mid)]))
if person['skills']==['Javascript','React']:
        print('He is a front end developer')
elif person['skills']==['Node','Python','MongoDB']:   
    print('He is a backend developer')
elif person['skills']==['Node','React','MongoDB']:
        print('He is a fullstack developer')
else:
    print('Unknown Title')
if person['is_married']==True and person['country']=='Finland':
    print('{} lives in {}.He is married'.format(person['first_name'],person['country']))