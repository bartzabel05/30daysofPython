dog={}
dog={'name':'bruno','color':'black','legs':4,'age':3}
student={
    'first_name':'Kartik',
    'last_name':'Kapoor',
    'gender':'Male',
    'age':20,
    'marital_status':False,
    'country':'India',
    'skills':["Javascript","C++","HTML","CSS"]
}
print(len(student))
print(type(student['skills']))
student['skills'].append('Python')
print(student['skills'])
keys=student.keys()
print(keys)
value=student.values()
print(value)
print(student.items())
student.popitem()
print(student)
student.pop('last_name')
print(student)
del student['marital_status']
print(student)
del student
print(student)