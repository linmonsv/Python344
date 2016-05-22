
# 8.3. Handling Exceptions
while True:
    try:
        x = 5#int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

"""
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
"""

try:
   raise Exception('spam', 'eggs')
except Exception as inst:
   print(type(inst))    # the exception instance
   print(inst.args)     # arguments stored in .args
   print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
   x, y = inst.args     # unpack args
   print('x =', x)
   print('y =', y)
"""
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
"""

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# 8.4. Raising Exceptions
raise NameError('HiThere')

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

# 8.5. User-defined Exceptions

class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

# 8.6. Defining Clean-up Actions
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause") # always,,,

divide(2, 1)
divide(2, 0)
divide("2", "1")

# 8.7. Predefined Clean-up Actions
for line in open("myfile.txt"):
    print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

