# =============================================================

# 1. Using self
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

student = Student("Hamza", 95)
student.display()

# =============================================================

# 2. Using cls

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")

a = Counter()
b = Counter()
Counter.display_count()

# =============================================================

# 3. Public Variables and Methods

class Car:
    def __init__(self, brand):
        self.brand=brand

    def start():
        print("Car starts")

car= Car()
car.start()
print(car.brand)

# ==============================================================

# 4. Class Variables and Class Methods

class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

a = Bank()
b = Bank()
Bank.change_bank_name("XYZ Bank")
print(a.bank_name)
print(b.bank_name)

# =============================================================

# 5. Static Variables and Static Methods    

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))

# ===========================================================

# 6. Constructors and Destructors

class Logger:
    def __init__(self):
        print("Logger initialized.")

    def __del__(self):
        print("Logger destroyed.")

logger = Logger()
del logger


# ==============================================================
# 7. Access Modifiers

class Employee:
    def __init__(self):
        self.name = "Ali"
        self._salary = 50000
        self.__ssn = "123-45-6789"

emp = Employee()
print(emp.name)          
print(emp._salary)      
# print(emp.__ssn)       
print(emp._Employee__ssn)  

# ==============================================================
# 8. The super() Function

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

t = Teacher("Sara", "Math")
print(t.name, t.subject)

# ==============================================================
# 9. Abstract Classes

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

r = Rectangle(4, 5)
print(r.area())

# ================================================================
# 10. Instance Methods

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

dog = Dog("Buddy", "Labrador")
dog.bark()

# ==============================================================
# 11. Class Methods

class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

Book.increment_book_count()
Book.increment_book_count()
print(Book.total_books)

# ==============================================================
# 12. Static Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

print(TemperatureConverter.celsius_to_fahrenheit(25))

# ===============================================================
# 13. Composition

class Engine:
    def start(self):
        print("Engine started.")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()

engine = Engine()
car = Car(engine)
car.start()

# ==============================================================
# 14. Aggregation

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Adeel")
dept = Department(emp)
print(dept.employee.name)

# ================================================================
# 15. MRO and Diamond Inheritance

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

obj = D()
obj.show()  

# ================================================================
# 16. Function Decorators

def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()

# ================================================================
# 17. Class Decorators

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    pass

p = Person()
print(p.greet())

# ================================================================
# 18. Property Decorators

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

product = Product(100)
print(product.price)
product.price = 150
print(product.price)
del product.price

# ================================================================
# 19. callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        return x * self.factor

m = Multiplier(3)
print(callable(m))   
print(m(10))           

# ================================================================
# 20. Custom Exception

class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")

try:
    check_age(16)
except InvalidAgeError as e:
    print("Exception:", e)

# ================================================================
# 21. Custom Iterable

class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

for num in Countdown(5):
    print(num)

# ================================================================

