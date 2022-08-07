#day3
age=20
height=6.0
comp=3+6j
base=int(input('Enter base:'))
height=int(input('Enter height:'))
area=base*height
print('Area of the traingle is:',area)
a=int(input('Enter side a'))
b=int(input('Enter side b'))
c=int(input('Enter side c'))
perimeter=a+b+c
print('Perimeter of the triangle is',perimeter)
length=input('Enter length')
width=input('Enter width')
area=int(length)*int(width)
perimeter=2*(int(length)+int(width))
print('Area:',area)
print('Perimeter:',perimeter)
x1,y1,x2,y2=2,2,6,10
m=(int(y2)-int(y1))/(int(x2)-int(x1))
x=0
y=x**2+6*x+9
print(y)
print(len('python')!=len('dragon'))
print('on' in 'python' and 'on' in 'dragon')
print('jargon' in 'I hope this course is not full of jargon')
print('on' not in 'python' and 'on' not in 'dragon')
fl=float(len('python'))
st=str(fl)
#check even
num=input('Enter number:')
if int(num)%2==0:
    print('Divisible by 2')
else:
    print('Not Divisible by 2')

conv=int(2.7)
print(7//3==conv)
print(type('10')==type(10))
print(int(9.8)==10)