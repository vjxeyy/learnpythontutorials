# integers 1 2 3 4 5
# float 1.2 5.6   9.5  10.50
# complex  5+2j
print(3 ** 3)  # - * / + ** %

# variables  , a-z , _ , watch , Watch
Watch_price = 500
Customer_Name = "vijay"

Watch1 = Name1 = 750

print(Customer_Name)
print(Customer_Name)

# strings
word = 'Hi'
word2 = "       my age is 13 , why can't i vote      "
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
# slicing , length , strip()
print(word3[-5:-1])  # (+)ranging --> ,  (-)ranging <--
print(len(para))
print(word2.strip())
print(word.lower())
print(word.upper())

a = 'raj'
print(a.replace('j', 'ju'))
print(a.split('a'))

print("hew" in word3)  # boolean data types

shop_jayam = 'carrot , tomato , chicken , mutton'
print("chicken" in shop_jayam)

a1 = 'hi'
a2 = ' vijay'
print(a1 + a2)  # concatenation operator

# operators and keywords
# boolean    means true or false
print(1 == 1)
# operators
# arithmetic + , -
# assignment =
# comparison > < >= <=
# logical and or not
# identity is is not
# membership in not in
# bitwise & | ^ ~ << >>

# normal assignment
number1 = 10
number1 /= 10

number2 = number1 + 20

# casting
a = float(10)
b = int(10.10)
c = str(120)
print(a, b, c)

# type
d = "h3"
print(type(d))

# list []
fruits = ['apple', 'orange', 'cherry']
fruits[1] = 'banana'
fruits.append("new")
print(fruits)

number = [11, 2, 20, 0]
number.sort(reverse=True)
print(number)

add = fruits + number
print(add)

# tuples ()
fruits = ('apple', 'orange', 'cherry')
print(fruits)

number = (11, 2, 20, 0)
print(number)

add = fruits + number
print(add)

# set {}
fruits = {'apple', 'orange', 'cherry'}
fruits.add('banana')
print(fruits)

number = (11, 2, 20, 0)
print(number)

# Dictionary , get
my_data = {
    "name": "vijay",
    "age": "13"
}
# my_data["age"] = 14
print(my_data.get("age"))

# if statements
age = 18
if age > 18:
    print("you can vote in election")
elif age == 18:
    print("apply for vote id")
else:
    print("you have to wait till 18")

a, b = 10, 20
if a == 10 or b == 20:  # and , or , nesting of if
    print("correct")
    if b == 20:
        print("hi")
else:
    print("incorrect")


# functions def
def addition(a, b):
    print(a + b)


def subtraction(a, b):
    print(a - b)


def hi(name):
    print("Hi," + name)


def fun(a):
    return a*100


addition(12, 10)
addition(100, 300)
subtraction(50, 25)
hi("balu")
print(fun(5))

# loops

name = 'karthik'

# for loop

for letters in name:
    print(letters)

fruits = ['apple', 'orange', 'banana']

for fruit in fruits:
    print(fruit)

for i in "hi, welcome":
    if i == ',':
# continue
        print(", is present")
#      break
    else:
        print(", is not present")

# range  5 - 0,1,2,3,4
for number in range(2, 6):
    print(number)

