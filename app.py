import streamlit as st

# ---------------------------------------------------
# Basic beginner-level Streamlit app to explain
# Python OOP topics along with example code
# ---------------------------------------------------

st.title("Python OOP Concepts")
st.text("A simple app to learn Object-Oriented Programming in Python")

# Dictionary holding topic name -> (explanation, code example)
topics = {
    "Abstraction": {
        "explanation": "Abstraction means hiding the implementation details and "
                        "only showing the necessary features. In Python, we use "
                        "'ABC' and '@abstractmethod' to force subclasses to "
                        "implement certain methods.",
        "code": '''from abc import ABC, abstractmethod

class Main(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def salary(self, amount):
        pass

    def intro(self):
        print(f"my name is {self.name}")

class Manager(Main):
    def salary(self, amount):
        print(f"my salary is {amount}")

m = Manager("Ahmad")
m.intro()
m.salary(10000)
'''
    },
    "Encapsulation": {
        "explanation": "Encapsulation means keeping data (attributes) private "
                        "and only allowing access through methods or properties. "
                        "In Python, we use a double underscore (__) to make an "
                        "attribute private.",
        "code": '''class Bank:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
        self.__balance = 0.0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

acc = Bank("user123", "pass456")
acc.balance = 5000
print(acc.balance)
'''
    },
    "Inheritance": {
        "explanation": "Inheritance allows a class (child) to reuse the "
                        "attributes and methods of another class (parent). "
                        "We use 'super()' to call the parent class's methods.",
        "code": '''class BankAcc:
    def __init__(self):
        self.acc_holder = "unknown"
        self.balance = 0

class PremiumBankAcc(BankAcc):
    def __init__(self):
        super().__init__()
        self.reward_points = 0

acc = PremiumBankAcc()
print(acc.acc_holder, acc.balance, acc.reward_points)
'''
    },
    "Polymorphism": {
        "explanation": "Polymorphism means different classes can define the "
                        "same method name, but each class implements it "
                        "differently. This lets us call the same method on "
                        "different objects and get different behavior.",
        "code": '''class SportsCar:
    def sound(self):
        print("vroooom")

class SuvCar:
    def sound(self):
        print("groooom")

def runner(obj):
    obj.sound()

objects = [SportsCar(), SuvCar()]
for obj in objects:
    runner(obj)
'''
    },
    "Constructors (__init__)": {
        "explanation": "The '__init__' method runs automatically when an "
                        "object is created. It is used to set up the initial "
                        "values (attributes) of an object.",
        "code": '''class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("Ahmad", 20, "Python")
print(s1.name, s1.age, s1.course)
'''
    },
    "Class Methods & Static Methods": {
        "explanation": "A '@classmethod' works on the class itself (using "
                        "'cls') instead of an instance. A '@staticmethod' is "
                        "a normal function placed inside a class that doesn't "
                        "need access to the class or instance.",
        "code": '''class Student:
    created_instances = 0

    def __init__(self, name):
        self.name = name
        Student.created_instances += 1

    @classmethod
    def update_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def is_adult(age):
        return age >= 18

s1 = Student("Ahmad")
Student.update_school("New School")
print(Student.is_adult(20))
'''
    },
    "Magic Methods (Operator Overloading)": {
        "explanation": "Magic methods (also called dunder methods, e.g. "
                        "'__add__', '__str__') let us define how built-in "
                        "operators and functions behave for our own objects.",
        "code": '''class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 6)
p2 = Point(3, 2)
p3 = p1 + p2
print(p3.x, p3.y)
'''
    },
    "Decorators (@property)": {
        "explanation": "The '@property' decorator lets a method be accessed "
                        "like an attribute. It is often used together with a "
                        "setter and deleter to control how a value is read, "
                        "changed, or removed.",
        "code": '''class Dect:
    def __init__(self, func):
        self.__func = func

    @property
    def func(self):
        return self.__func

    @func.deleter
    def func(self):
        print("Deleting function...")
        del self.__func

d1 = Dect(lambda x: x + 1)
print(d1.func(5))  # 6
'''
    },
}

# Sidebar to pick a topic
st.sidebar.header("Choose a Topic")
selected_topic = st.sidebar.selectbox("OOP Topic", list(topics.keys()))

# Main content
st.subheader(selected_topic)
st.write(topics[selected_topic]["explanation"])

st.subheader("Example Code")
st.code(topics[selected_topic]["code"], language="python")

st.divider()
st.text("Select a different topic from the sidebar to keep learning!")