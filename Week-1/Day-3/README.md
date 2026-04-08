# OOPS CONCEPT IN PYTHON..

:- Class and Object
-A class is a collection of objects. class is a blueprint used to create objects.
A class defines a set of attributes and methods that the created objects (instances) can have.  
-An object is an instance of a class that contains actual data.

Real-Life Analogy
Class = Blueprint of a house
Object = Actual house built from blueprint

# Constructor (__init__)

A constructor is a special method automatically called when an object is created.It is used to initialize values.

# Instance vs Class Variables
Definition
Instance Variable → unique for each object
Class Variable → shared by all objects

# Types of method
Python has 3 types of methods:
# Instance method:- 
-Works with object (instance) data
-Uses the self parameter
-Can access and modify instance variables
Key Points
-Called using object
-Has access to self
-Used for object‑specific behavior
# Class method:-
-Works with class-level data
-Uses @classmethod decorator
-Takes cls as parameter (refers to the class)
-Affects all objects, not a single object
Key Points
-Accesses class variables
-Used to modify class state
-Called using class name
# Static method:-
-Independent method
-No access to instance (self) or class (cls)
-Uses @staticmethod decorator

# Inheritance
Inheritance allows a class (child class) to acquire properties and methods of another class (parent class). It supports hierarchical classification and promotes code reuse.

# Polymorphism
Polymorphism means "same operation, different behavior." It allows functions or methods with the same name to work differently depending on the type of object they are acting upon.
# Method Overloading vs Method Overriding
# What is Method Overloading?
Method overloading means:Same method name but different parameters

Important (Python fact):
Python does NOT support traditional method overloading like Java or C++.
Instead, Python achieves it using:
Default arguments
*args

# Method Overriding
What is Method Overriding?
Method overriding means:

Same method name and parameters in parent and child class,
but child class redefines the method behavior.

Happens due to inheritance
Resolved at runtime

#  Encapsulation
Encapsulation is the bundling of data (attributes) and methods (functions) within a class, restricting access to some components to control interactions. A class is an example of encapsulation as it encapsulates all the data that is member functions, variables, etc.

# Data Abstraction 
Abstraction hides the internal implementation details while exposing only the necessary functionality. It helps focus on "what to do" rather than "how to do it."