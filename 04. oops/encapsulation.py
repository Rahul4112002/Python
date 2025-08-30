'''Encapsulation Example'''

class Factory:
    __secret = 'This is private'
    def show(self):
        print(Factory.__secret)
        
obj = Factory()
obj.show()

