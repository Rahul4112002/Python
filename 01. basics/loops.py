'''Loops in python'''

#for loop table - 5
n = 5 
for i in range(1,11):
    print(f"5 X {i} = {n*i}")


#iterating through a string
name = "rahul"
for char in name:
    print(char)
    
    
#sum of first n numbers
n = 5
s = 0
for i in range(n):
    s = s+i
print(s)

# Factorial
n = 5
f = 1
for i in range(1,n+1):
    f = f*i
print("Factorial: ", f)

#while loop - counting
a = 1
while a<=10:
    print(a)
    a += 1
    
# Reverse number using while
num = 1234
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed =", rev)