"""Keyword Arguments (**kwargs)"""

def information(**kwargs):
    print("Your information:")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

information(name="Akarsh", age=23, designation="AI/ML")
