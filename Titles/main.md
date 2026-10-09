#Variables
- A variable in Python is a name that refers to an object in memory
 - ~~`age` is a box containing 22~~
 - age ───────► 22

- Python doesn't require you to declare a variable's type.
- Python determines that `x` currently refers to an `int` object.
 - `x = "Ahmad"` infact it is `x ─────► "Ahmad"`
 - That's why Python is called dynamically typed.

- Variables are references to objects
    - `a = 10` 
    - `b = a`
        ┌───────┐
a ─────►│       │
        │  10   │
b ─────►│       │
        └───────┘
- Both names refer to the same object in this situation, You can investigate identity using `id()` \ `print(id(a))`

