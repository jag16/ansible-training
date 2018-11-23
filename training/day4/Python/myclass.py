#!/usr/bin/python

class MyClass:
    def __init__(self):
        print("Constructor")

    def sayHello(self, message):
        print (message)


if __name__ == "__main__":

    obj = MyClass()  # Creates an instance on MyClass

    obj.sayHello( "Hello My Class" )
