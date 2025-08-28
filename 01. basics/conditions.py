"""Conditional Statements"""

a = 6
if a > 10:
    print("I will do task A")
else:
    print("I will do task B")

money = 20
if money == 10:
    print("I will have a choco bar icecream")
elif money == 20:
    print("I will have a mangodolly")
elif money == 30:
    print("I will have a frosty")
else:
    print("I will have a cone")

num1 = 10
num2 = 15
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are same")

gen = "M"
if gen.lower() == 'm':
    print("Good morning SIR")
elif gen.lower() == 'f':
    print("Good morning MAM")
else:
    print("Unidentified gender")

num = 11
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
