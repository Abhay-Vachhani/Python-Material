# Abstract Methods and Abstract Class, Interface

## Abstract Method:

- An abstract method is a method whose action is redefined in the sub classes as per the requirement of the objects

- Generally abstract methods are written without body since their body will be defined in the sub classes

## Abstract Class:

- An abstract class is a class that generally contains some abstract methods

- As abstract methods do not contain body of the method, PVM cannot estimate the requirement of the memory

- So PVM cannot create objects to an abstract class

- After creating an abstract class, we should create sub classes and body of all the abstract methods must be written

- Now, it will be possible to create an object to the sub classes

- An abstract class may contain an abstract method

- It may also contain a concrete method along with the abstract method

- All the abstract classes should be derived from the meta class 'ABC' which belongs to 'abc' ( Abstract Base Class ), We should import this module into our program


## Interfaces in Python:

- We know that an abstract class is an class which contains some abstract methods as well as concrete methods also

- Now, imagine a class with only abstract methods and there are no concrete methods, it is known as interface

- In other words we can say that a class with only abstract methods and no concrete methods is known as interface

- Python does not required any type of keywords (like interface in java) to declare class as interface



# Difference between Abstract class and Interface:

| Abstract Class                                                                                 | Interface                                                                                                  |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| An abstract class can contain an abstract method.it may also contain concrete method           | An interface can only contain an abstract methods. It will become abstract if it contain a concrete method |
| It is used when there some common features shared by all objects                               | It is used when all the features need to be implemented differently for different objects                  |
| It is programmers responsibility to create a child class for the features of an abstract class | Any third party will take a responsibility for creating a child class                                      |
| It is comparatively faster as sub classes are written by the programmer him self               | It is comparatively slower as writing the sub classes is done by some other programmers                    |
| A decorator like @abstractmethod should be written before writing an abstract class            | It is not  so with an interface                                                                            |
