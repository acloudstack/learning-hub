
class MyClass:
    '''This is a demo Class '''

    # class attribute
    class_attribute = 10

    # instance attribute
    def __init__(self, instance_attribute_1 = 0, instance_attribute_2 = 0):
        self.instance_attribute_1 = instance_attribute_1
        self.instance_attribute_2 = instance_attribute_2

    # class function
    def class_function(self):
        print('This is a class function.')
        return True


def main():
    # Output: 10
    print(MyClass.class_attribute)

    # Output: <function Person.greet>
    print(MyClass.class_function)

    # Output: "This is a person class"
    print(MyClass.__doc__)

    myobject = MyClass()
    #myobject.class_function()


if __name__ == '__main__':
    main()


# Class:        A class is a blueprint for the object.

# Object:       An object (instance) is an instantiation of a class. 
#               When class is defined, only the description for the object is defined. 
#               Therefore, no memory or storage is allocated.

# Method:       Methods are functions defined inside the body of a class. 
#               They are used to define the behaviors of an object.

# Inheritance:  Inheritance is a way of creating a new class for using details of an 
#               existing class without modifying it. 
#               The newly formed class is a derived class (or child class).
#               Similarly, the existing class is a base class (or parent class).

# Encapsulation:    Using OOP in Python, we can restrict access to methods and 
#                   variables. This prevents data from direct modification which 
#                   is called encapsulation. In Python, we denote private 
#                   attributes using underscore as the prefix i.e 
#                   single _ or double __.

# Polymerphism: Polymorphism is an ability (in OOP) to use a common interface 
#               for multiple forms (data types).
#               Suppose, we need to color a shape, there are multiple shape options 
#               (rectangle, square, circle). 
#               However we could use the same method to color any shape. 
#               This concept is called Polymorphism.
# 

# Test fixture- the preparation necessary to carry out test(s) and 
#               related cleanup actions.

# Test case -       the individual unit of testing.

# A Test suite -    collection of test cases, test suites, or both.

# Test runner -     component for organizing the execution of tests and 
#                   for delivering the outcome to the user.