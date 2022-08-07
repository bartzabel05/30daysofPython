# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['TCS','Infosys','HCL'])
print(it_companies)
it_companies.remove('TCS')
print(it_companies)
#remove gives error if element not present in set whereas discard doesnt produce error in that case
a=list(A)
b=list(B)
c=a+b
C=set(c)
print(C)
print(A.intersection(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A
del B
ages=set(age)
print(len(ages))
print(len(age))
print(len(ages)>len(age))
str={'I','am','a','teacher','and','I','love','to','inspire','and','teach','people'}
print(str)