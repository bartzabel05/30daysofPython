empty=tuple()
bros=('sam','brim','breach')
sis=('lana','mia','raze','jett')
siblings=bros+sis
print(len(siblings))
siblings_copy=list(siblings)
siblings_copy.append('Richard')
siblings_copy.append('Rachel')
family_members=tuple(siblings_copy)
print(family_members)
*siblings,father,mother=family_members
print(father)
print(mother)
print(siblings)
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products=('Milk','Cheese','Butter','Ghee')
food_stuff_tp=fruits+vegetables+animal_products
print(food_stuff_tp)
food_stuff_lt=list(food_stuff_tp)
mid=(len(food_stuff_lt)-1)/2
middle=food_stuff_lt[int(mid)]
print(middle)
first_three=food_stuff_lt[0:3]
last_three=food_stuff_lt[10:]
print(first_three)
print(last_three)
del food_stuff_tp
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Iceland' in nordic_countries)
print('Estonia' in nordic_countries)