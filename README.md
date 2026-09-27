OOP in Python — Practice Repo
=============================

A collection of small Python scripts for practicing core Object-Oriented Programming (OOP) concepts — written while learning things like abstraction, encapsulation, polymorphism, inheritance, decorators, constructors, and magic methods.

Folder Structure
----------------

    OOP/
    ├── code/            # (supporting / earlier code experiments)
    ├── topics/          # main practice scripts, one concept per file
    │   ├── abs.py
    │   ├── abstract.py
    │   ├── const.py
    │   ├── const_p.py
    │   ├── decorat.py
    │   ├── encaps.py
    │   ├── main.md
    │   ├── mthd.py
    │   ├── polyMorph.py
    │   ├── self_proj.py
    │   └── self.py
    └── .gitignore
    

What each file covers
---------------------

> Note: descriptions below are based on the current contents of each script. Update them as the files evolve.

File

Topic

What it demonstrates

`abs.py`

Abstraction

An abstract base class `main` (using `ABC` + `@abstractmethod`) with a `salary()` method that subclasses `manager` and `dev` must implement, plus a shared `intro()` method.

`abstract.py`

Abstraction & Duck Typing

Another abstract base class with an abstract `sound()` method, implemented differently by `sports_car` and `suv_car`, called through a generic `runner(obj)` function.

`const.py`

Constructors

Basic use of `__init__` to set default attribute values (`bank_acc`), and extending it with `super().__init__()` in a subclass (`premium_bank_acc`).

`const_p.py`

Constructors (practice project)

An interactive, menu-driven console program that creates different types of bank accounts (basic, premium, fully customized) based on user input, using constructors with parameters.

`decorat.py`

Decorators / Properties

Use of `@property`, `.setter`, and `.deleter` to control access to a private attribute (`dect` class wrapping a function).

`encaps.py`

Encapsulation

Private attributes (`__name`, `__balance`, etc.) protected behind `@property`/setter methods in a `bank` class, plus a comparison version (`bank1`) using plain getter/setter methods instead of properties.

`mthd.py`

Class & Static Methods

A `student` class showing instance methods, a class-level counter (`created_instances`), `@classmethod` (`update_school`), and `@staticmethod` (`total_students`, `is_adult`, `is_course`).

`polyMorph.py`

Polymorphism & Magic Methods

`rectangle`, `square`, `circle`, and `point` classes sharing an `area()` method used via duck typing (`show_area()`), plus operator overloading with `__add__` on the `point` class.

`self_proj.py`

Practice Project

A `student` class with an interactive Q&A loop (`disp()`) that counts and responds to user questions until an exit keyword is entered.

`self.py`

Understanding `self`

Minimal examples showing how `self` and `__init__` work when creating class instances.

`main.md`

Notes

Markdown notes/documentation for the topics covered in this folder.

Concepts Covered
----------------

*   Abstract Base Classes (`ABC`, `@abstractmethod`)
*   Inheritance & `super()`
*   Encapsulation (private attributes, getters/setters, `@property`)
*   Polymorphism & Duck Typing
*   Constructors (`__init__`) and object initialization patterns
*   Class methods vs. Static methods vs. Instance methods
*   Magic/dunder methods (e.g. `__add__`)
*   Decorators

How to Run
----------

Each script can be run independently:

    python topics/abs.py
    

Some scripts (like `const_p.py` and `self_proj.py`) are interactive and will prompt for input in the terminal.

Status
------

Work in progress — this repo is used for ongoing OOP practice, so file contents and structure may change over time.