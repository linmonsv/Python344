# 6. Modules
import fibo
fibo.fib(1000)
fibo.fib2(1000)
print(fibo.__name__)

# 6.1. More on Modules
from fibo import fib, fib2
fib(500)

from fibo import *
fib(500)

# 6.1.1. Executing modules as scripts

# run a Python module with arguments
# fibo.py __name ==

# If the module is imported, the code is not run:

# 6.1.2. The Module Search Path

# 6.1.3. “Compiled” Python files
# __pycache__ directory

# 6.3. The dir() Function
import fibo, sys
# find out which names a module
print(dir(fibo))

print(dir(sys))

# Without arguments, dir() lists the names you have defined currently
a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
print(dir())

# dir() does not list the names of built-in functions and variables.
# If you want a list of those, they are defined in the standard module builtins:
import builtins
print(dir(builtins))
