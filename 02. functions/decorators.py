'''Funtion Decorators'''

def decorate(func):
    def wrapper(*args,**kwargs):
        print("Before funtion call")
        func(*args, **kwargs)
        print("After funtion call")
    return wrapper

@decorate
def addition(a,b):
    print(f'Your total is {a+b}')
addition(12,15)