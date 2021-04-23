""" Write a Python program to create two empty classes, Student and Marks. 
Now create some instances and check whether they are instances of the said classes or not. 
Also, check whether the said classes are subclasses of the built-in object class or not. """

class Student:

    #inner class
    class Details:
        pass

class Marks:
    pass

class14Student = Student()                  # Student instance
class14StudentMarks = Marks()               # Marks instance 
class14StudentDetails = Student().Details() #instance for inner class

print(isinstance(class14Student, Student))                  # True as class14Student is an instance of Student
print(isinstance(class14Student, Marks))                    # False as class14Student is NOT an instance of Marks
print(isinstance(class14StudentDetails, Student))           # False as class14StudentDetails is NOT an instance of Student
print(isinstance(class14StudentDetails, Student.Details))   # True as class14StudentDetails is an instance of inner class in Student

print(type(class14Student))
print(type(class14StudentMarks))
print(type(class14StudentDetails))


