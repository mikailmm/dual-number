# Simple Dual Number Library

This project is an exercise of using Git and GitHub and also using Python's magic dunder methods to create a simple Dual Number library. Relations and operations that are implemented are:
- Addition and subtraction
- Multiplication

## Example
```
from dual_number import Dual
a = Dual(3, 1)
b = Dual(2, 4)
print(f'{a=} {b=}') # a=3+ε b=2+4ε
print(f'{a*b=}') # a*b=6+14ε
```

Further examples can be seen on [notebook.ipynb](notebook.ipynb)

Source: https://en.wikipedia.org/wiki/Dual_number