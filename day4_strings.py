a="Thirty"
b="Days"
c="Of"
d="Python"
g="Coding"
h="For"
i="All"
e="{} {} {} {}".format(a,b,c,d)
f="{} {} {}".format(g,h,i)
print(f)
print(e)
company="Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.index("Coding"))
print(company.find("Coding"))
comp=company.replace("Coding","Python")
print(comp)
com=comp.replace("All","Everyone")
print(com)
print(company)
print(company.split(" "))
cm="Facebook,Google,Microsoft,Apple,IBM,Oracle,Amazon"
print(cm.split(","))
print(company[0])
print(company[len(company)-1])
print(company[10])

def fxn(str):
    op=str[0]
    for i in range(1,len(str)):
        if str[i-1]==" ":
         op+=str[i]
    op=op.upper()
    return op
print(fxn(company))
print(fxn(com))

print(company.index("C"))
print(company.rfind("i"))
abc='You cannot end a sentence with because because because is a conjunction'
print(abc.index("because"))
print(abc.find("because"))
print(abc.rfind("because"))
print(abc[31:54])
print(company.startswith("Coding"))
print(company.endswith("coding"))
df='\tCoding For All\t'  
print(df.expandtabs(0))
de='   Coding For All      ' 
print(de[3:18])
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
ef=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(ef))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("Name\tAge\tCountry\tCity\nAsabaneh\t250\tFinland\tHelsinki")
radius=10
area=3.14*radius**2
print("The area of a circle with radius {} is {} meters square".format(radius,area))
print("{}+{}={}".format(8,6,8+6))
print("{}-{}={}".format(8,6,8-6))
print("{}*{}={}".format(8,6,8*6))
print("{}/{}={}".format(8,6,8/6))
print("{}%{}={}".format(8,6,8%6))
print("{}//{}={}".format(8,6,8//6))
print("{}**{}={}".format(8,6,8**6))