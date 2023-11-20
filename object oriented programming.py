#object oriented prgramming: easy to manipulate complicated code, but computation takes longer. Example follows
#declarative programming: enhances os, ex: db languages. imperative programming: uses os, ex: python
#oop uses class -> idea, and object(instances) -> real thing
#creating a class 
class Dog:
    pass
#making an instance
ozzy = Dog() 
print(ozzy) 
#setting instance attributes
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age #each object can have distinct attributes 
ozzy = Dog('Ozzy', 2)
#then attributes can be returned
print(ozzy.name, ozzy.age)
#method defining
#methods -> functions for class objects  
class Dog:
    def bark(self): #self refers to the instance that the method is applied 
        print('bark bark!')
ozzy = Dog()
ozzy.bark()
#passing attributes to methods 
class Dog:
    def __init__(self, name, age):  
        self.name = name
        self.age = age
    def bark(self):
        print("bark bark!")
    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")
    def birthday(self):
        self.age +=1
    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self
#now one can use methods with attributes 
ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)
ozzy.setBuddy(filou)
print(ozzy.buddy.name)
print(ozzy.buddy.age)
print(filou.buddy.name)
#class inheritance -> enables parent attributes and methods 
class Animal: 
    def __init__(self, type, breed):
        self.type = type 
        self.breed = breed
    def make_sound(self):
        if self.breed == 'dog':
            print('bark!')
class Dog(Animal): #Animal is the parent class, inheritance can occur 
    def __init__(self, name, type, breed):
        super().__init__(type, breed) #use super() to access parent attributes and get methods from parent class 
        self.name = name
    def bark(self):
        super().make_sound()
ozzy = Dog(name = 'ozzy', type = 'mammal', breed = 'dog')
print(ozzy.type)
ozzy.bark()
ozzy.make_sound()
#class attribute 
class Dog: 
    Nationality = 'Kor' #no self or not under __init__ -> all instances will have this attribute 
ozzy = Dog()
print(Dog.Nationality == ozzy.Nationality)
#class attribute can have the same name as instance attribute
#but method cannot share the same name 
#class and static methods 
class Animal:
    type = 'life'
    @staticmethod #this method is static 
    def static_factory():
        object = Animal()
        object.type = Animal.type
        return object #the classes used in the method is named
    @classmethod 
    def class_fatory(cls):
        object = cls()
        object.type = cls.type
        return object #the classes used in the method can vary 
class Dog(Animal):
    type = 'animal'
static_animal = Animal.static_factory()
static_dog = Dog.static_factory() #the result is fixed 
class_animal = Animal.class_fatory()
class_dog = Dog.class_fatory() #the result changes for each class
print(static_animal.type, static_dog.type, class_animal.type, class_dog.type, sep = '\n')
#visibility -> not actual feature but convention 
self.attr #public
self._attr #protected
self.__private #private -> this mangles with class name 
#property -> make an applied method like an attribute 
#meaning no argument can pass through the method
class Dog:
    @property
    def sounds_like(self):
        print('bark!')
ozzy = Dog()
ozzy.sounds_like
#magic methods 
#constructor 
__init__() #no argument format, used when creating an instance 
#destroyer
#not used often since Python uses variable memory -> hard to delete all instances and variables assigned for the class  
__del__() 
#indexing item 
__getitem__() #can override indexing and slicing of the class 
__setitem__() #changes the result of instance[n] or instance[n] = x
#length 
__len__() #can override len(instance)
#typing 
__str__() #override str()
__int__() #override int()
__bool__() #override bool()
__float__() #override float()
#order
__lt__() #override <
__le__() #override <=
__gt__() #override >
__ge__() #override >=
__eq__() #override ==
__ne__() #override !=
#operators 
__add__() #overrides +
__sub__() #overrides -
__mul__() #overrides *
__iadd__() # overrides += 
#callable 
__call__() #enables instance() -> function like
#iterable 
__iter__() #overrides iter()
__next__() #overrides next()
#context manager 
#with loop managing
class Dog:
    def __init__(self, name):
        self.name = name
    def __enter__(self): #when instance enters the with loop 
        print(f'my name is {self.name}')
        return self
    def __exit__(self, exc_type, exc_value, trace): #when instance leaves the with loop 
        print('bye')
ozzy = Dog('ozzy')
with ozzy:
    ozzy.name = 'not ozzy'
    print(ozzy.name)
with Dog('johnny') as johnny: #starts __enter__() with johnny = Dog('johnny')
    pass