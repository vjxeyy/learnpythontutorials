# loops

name = 'vijay'

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
for number in range(2, 20, 2):   # can be used in tables
    print(number)

for number in range(5):
    print(number)
    for i in range(2):
        print(i)
else:
    print('all numbers are finished')
