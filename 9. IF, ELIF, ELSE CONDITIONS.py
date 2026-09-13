# if statements
age = 18
if age > 18:
    print("you cant vote in election")
elif age == 18:
    print("apply for vote id")
else:
    print("you have to wait till 18")


a, b = 10, 20       # and, or
if a == 100 or b == 20: # and, or, nesting of if
    print("correct")
    if b == 20:
        print("hi")
else:
    print("incorrect")