import random,string
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