l1=[]
l2=[1,2,3,4,5,6]
print(len(l2))
print(l2[0])
last=len(l2)-1
mid=last/2
print(l2[int(mid)])
print(l2[last])
mixed_data_types=['Kartik',250,6.0,False]
it_companies=['Facebook','Google','Microsoft','Apple']
print(it_companies)
first=0
last=len(it_companies)-1
mid=(last-first)/2
print(it_companies[first])
print(it_companies[int(mid)])
print(it_companies[last])
it_companies[2]='IBM'
print(it_companies)
it_companies.append('Microsoft')
print(it_companies)
last=len(it_companies)-1
it_companies.insert(int(last/2),'Oracle')
print(it_companies)
it_companies[0]=it_companies[0].upper()
print(it_companies)
print(' # '.join(it_companies))
print('Oracle' in it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[3:])
m=len(it_companies)-1
print(it_companies[int(m/2)])
it_companies.remove('Oracle')
print(it_companies)
del it_companies[int(m/2)]
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack=front_end+back_end
print(full_stack)
full_stack_copy=full_stack.copy()
print(full_stack_copy)
country=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first,second,*scandic=country
print(first)
print(second)
print(scandic)
fh=country[0:4]
sh=[country[4:7]]
print(fh)
print(sh)
md=(len(country)-1)/2
print(country[int(md)])

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.append(ages[0])
ages.sort()
print(ages)
last=len(ages)-1
ages.append(ages[last])
ages.sort()
print(ages)
avg=(19+19+19+20+22+24+24+24+25+25+26+26)/12
print(avg)
last=len(ages)-1
median=last/2
print(ages[int(median)])
range=ages[int(last)]-ages[0]
print(range)
m1=ages[0]-avg
m2=ages[int(last)]-avg
print(m1>m2)