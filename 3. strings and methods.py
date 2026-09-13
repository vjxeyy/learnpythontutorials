# strings
word = 'Hi'
word2 = "    my age is 13, why can't i vote    "
para = """ this
is
my para 
"""

para2 = """hello I am vijay from India, My age is 13 and 
I love doraemon cartoon, I am watching it from 5 years ago.
------------
--Doraemon-----------------
------------
"""
word3 = "hello, world"
# slicing ,  length , strip()
print(word3[-5:-1])  # range ,  negative ranging
print(len(para))
print(word2.strip())

print(word.lower())
print(word.upper())

a, b = 'raj', 'vijay'
print(a.replace('j', 'ju'))

print(a.split('a'))

print('hew' in word3)

shop_jayam = 'carrot , tomato , chicken , mutton'
print("chicken" in shop_jayam)

a1 = 'hi'
a2 = ' vijay'
print(a1 + a2)  # concatenation operator
