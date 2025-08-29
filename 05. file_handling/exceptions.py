'''Exception Handling Examples'''

#Example 1: Division by zero handling
# a = int(input("Enter a number: "))
# try:
#     print(10/a)
# except Exception as err:
#     print(f"Error occured: {err}")
# else:
#     print("No exception, division successful")
# finally:
#     print("This will always run")
# print("PRogram continue....")

#Example 2: Raising custom exception
age = int(input("Enter your age: "))
try:
    if age<10 or age>18:
        raise ValueError("Your age must be between 10 and 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"Error: {err}")

print("Club registration ended")