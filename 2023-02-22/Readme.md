## Lab(Lecture)

# Garbage collection in Python:
- Garbage collection is a module in python that is useful to delete objects from memory which are not used in the program

- The module of garbage collection in python is known as 'gc'

- Garbage collector maintain the count of each object regarding number of times it is referred (used)

- When an object is used 3 times then its reference count would be 3

- Count greater than 0 means an object is being used or referred.

- Garbage collector runs automatically

- But in the case when more number of objects is created and if the system runs out of memory then automatic garbage collector will not run

- In this case manual garbage collection is to be used

- Manual garbage collection is of two types
    1) Time based manual garbage collection
    2) Event based manual garbage collection

#### 1) Time based manual garbage collection : 
    If the garbage collector called in certain intervals of time, it is called time based manual garbage collection

#### 2) Event based manual garbage collection : 
     If the garbage collector is called in the basis of event for example when user disconnects from an application it is called event based garbage collection

- If garbage collector is called frequently, it will slow down the program execution

# How Python sees variables
- In programming languages like C, Java, etc... the concept of variable is connected to memory location

- This kind of programming languages uses variable as a storage box

- Suppose that we write a = 7 then 'a' is allocated some memory and 7 is stored into it

![n](https://)

- Now suppose we change value of 'a', a = 34 then it maybe visualized as below

![alt](https://)

- When we assign one variable to another variable (b = a) then it may be visualized as below

![alt](https://)

- But in python variable is seen as a tag (name) that is tied to some value. For example a = 7, in python it would be like 'a ---> 7'

![alt](https://)

- Now suppose we change value of 'a', a = 34 then the tag is simply change to the new value

![alt](https://)

- Assigning one variable to another (b = a) makes a new tag bound to the same value

![alt](https://)

- Python has 'tags' to represents the values

- Python is using memory efficiently

