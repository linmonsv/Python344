# Python344

# The Python Tutorial

### 2.1.1. Argument Passing

### 3.1.2. Strings

String literals can span multiple lines.

Two or more string literals next to each other are automatically concatenated.

### 3.1.3. Lists

You can also add new items at the end of the list, by using the append() method

## 3.2. First Steps Towards Programming

The keyword argument end can be used to avoid the newline after the output, 

or end the output with a different string:

## 4.2. for Statements

If you need to modify the sequence you are iterating over while inside the loop

(for example to duplicate selected items),

it is recommended that you first make a copy.

Iterating over a sequence does not implicitly make a copy.

The slice notation makes this especially convenient

## 4.3. The range() Function

The given end point is never part of the generated sequence;

range(10) generates 10 values,

the legal indices for items of a sequence of length 10.

It is possible to let the range start at another number,

or to specify a different increment

(even negative; sometimes this is called the ‘step’):

## 4.5. pass Statements

* required syntactically

* for creating minimal classes* 

* a place-holder

## 4.6. Defining Functions

This value can be assigned to another name which can then also be used as a function

## 4.7. More on Defining Functions

### 4.7.1. Default Argument Values

The default values are evaluated at the point of function definition in the defining scope

**Important warning**: The default value is evaluated only once

### 4.7.2. Keyword Arguments

using keyword arguments of the form kwarg=value

In a function call, keyword arguments must follow positional arguments

When a final formal parameter of the form **name is present, 

it receives a dictionary (see Mapping Types — dict) containing all keyword arguments 

except for those corresponding to a formal parameter. 

This may be combined with a formal parameter of the form *name (described in the next subsection) 

which receives a tuple containing the positional arguments 

beyond the formal parameter list. 

(*name must occur before **name.) 

### 4.7.3. Arbitrary Argument Lists

These arguments will be wrapped up in a tuple 

### 4.7.4. Unpacking Argument Lists

The reverse situation occurs when the arguments are already in a list or tuple 

but need to be unpacked for a function call requiring separate positional arguments

### 4.7.5. Lambda Expressions

* uses a lambda expression to return a function.

* Another use is to pass a small function as an argument

### 4.7.6. Documentation Strings

The **first line** should always be a short, concise summary of the object’s purpose.

If there are more lines in the documentation string, **the second line** should be blank, 

visually separating the summary from the rest of the description. 

The following lines should be one or more paragraphs describing the object’s calling conventions, its side effects, etc.

```Python
print(my_function.__doc__)
```

### 4.7.7. Function Annotations

Annotations are stored in the __annotations__ attribute of the function as a dictionary and have no effect on any other part of the function

## 4.8. Intermezzo: Coding Style

1. Use 4-space indentation, and no tabs

2. Wrap lines so that they don’t exceed 79 characters

3. Use blank lines to separate functions and classes, and larger blocks of code inside functions

4. When possible, put comments on a line of their own

5. Use docstrings

6. Use spaces around operators and after commas

7. Name your classes and functions consistently; CamelCase and lower_case_with_underscores

8. Don’t use fancy encodings 

9. don’t use non-ASCII characters 

## 5.1. More on Lists

Remove the item at the given position in the list, and return it.

If no index is specified, a.pop() removes and returns the last item in the list

## 5.1.3. List Comprehensions

```Python
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = [x**2 for x in range(10)]
print(squares)
```

# 5.2. The del statement

```Python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
```

# 5.4. Sets

A set is an unordered collection with no duplicate elements

# 5.5. Dictionaries

# 5.6. Looping Techniques

```Python

# When looping through dictionaries
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# When looping through a sequence
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# To loop over two or more sequences at the same time
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

# To loop over a sequence in reverse
for i in reversed(range(1, 10, 2)):
    print(i)

# To loop over a sequence in sorted order
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

# To change a sequence you are iterating over while inside the loop
words = ['cat', 'window', 'defenestrate']
for w in words[:]:  # Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)

```

# 6.1. More on Modules
# Note
For efficiency reasons,
each module is only imported once per interpreter session.
Therefore, if you change your modules, you must restart the interpreter –
or, if it’s just one module you want to test interactively, use imp.reload(),
e.g. import imp; imp.reload(modulename).


# 6.1.2. The Module Search Path

# 6.1.3. “Compiled” Python files

__pycache__ directory

Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures

* You can use the -O or -OO

* A program doesn’t run any faster when it is read from a .pyc or .pyo file than when it is read from a .py file;
the only thing that’s faster about .pyc or .pyo files is the speed with which they are loaded.

* The module compileall can create .pyc files (or .pyo files when -O is used) for all modules in a directory.

* more detail in PEP 3147

# 6.2. Standard Modules
```
>>> import sys
>>> sys.ps1
'>>> '
>>> sys.ps2
'... '
>>> sys.ps1 = 'C> '
C> print('Yuck!')
Yuck!
C>
```

# 6.4. Packages

1. When importing the package, Python searches through the directories on sys.path looking for the package subdirectory.

2. The __init__.py files are required to make Python treat the directories as containing packages

## 6.4.1. Importing * From a Package

* time

* size

# __init__.py
# This would mean that from sound.effects import * would import the three named submodules of the sound package.
'''
__all__ = ["echo", "surround", "reverse"]
'''

## 6.4.2. Intra-package References

```python
from . import echo
from .. import formats
from ..filters import equalizer
```

# 7.1. Fancier Output Formatting
```python
# Passing an integer after the ':' will cause that field to be a minimum number of characters wide
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))

# be formatted by name instead of by position
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
```
but the 'd' what's means ?

# 7.2. Reading and Writing Files
```python
f = open('workfile', 'w')

# 7.2.1. Methods of File Objects
f.read()
f.readline()

for line in f:
    print(line, end='')

f.write('This is a test\n')

value = ('the answer', 42)
s = str(value)
f.write(s)

```

# It is good practice to use the with keyword when dealing with file objects

# 7.2.2. Saving structured data with json
# Note The JSON format is commonly used by modern applications to allow for data exchange.
# Many programmers are already familiar with it, which makes it a good choice for interoperability.
```
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'

json.dump(x, f)

x = json.load(f)

```

# 8. Errors and Exceptions

There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

* A finally clause is always executed before leaving the try statement, 
* whether an exception has occurred or not. 

## 8.7. Predefined Clean-up Actions
```python
for line in open("myfile.txt"):
    print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

# 10. Brief Tour of the Standard Library

1. os.getcwd()

2. glob.glob('*.py')

3. re.findall

4. random.sample(range(100), 10)

5. from datetime import date

## **10.10. Performance Measurement**

from timeit import Timer

## **10.11. Quality Control**

import doctest

import unittest

# 11.5. Logging

New filters can select different routing based on message priority: 

DEBUG, INFO, WARNING, ERROR, and CRITICAL.

# 11.8. Decimal Floating Point Arithmetic

* financial applications and other uses which require exact decimal representation, 
* control over precision, 
* control over rounding to meet legal or regulatory requirements, 
* tracking of significant decimal places, or 
* applications where the user expects the results to match calculations done by hand. 

# 12.2. Creating Virtual Environments

To create a virtualenv, decide upon a directory where you want to place it and run pyvenv with the directory path:

```
pyvenv tutorial-env
```

Once you’ve created a virtual environment, you need to activate it.

```
# On Windows, run:

tutorial-env/Scripts/activate

# On Unix or MacOS, run:

source tutorial-env/bin/activate

```

'''
-> source ~/envs/tutorial-env/bin/activate
(tutorial-env) -> python
Python 3.4.3+ (3.4:c7b9645a6f35+, May 22 2015, 09:31:25)
  ...
>>> import sys
>>> sys.path
['', '/usr/local/lib/python34.zip', ...,
'~/envs/tutorial-env/lib/python3.4/site-packages']
>>>
'''

# 12.3. Managing Packages with pip

```
(tutorial-env) -> pip search astronomy
```

## pip has a number of subcommands:
* “search”,
* “install”,
* “uninstall”,
* “freeze”,
* etc. (Consult the Installing Python Modules guide for complete documentation for pip.)

```
# the latest version
pip install novas

# a specific version
pip install requests==2.6.0

# upgrade
-> pip install --upgrade requests

# pip uninstall

# display information about a particular package
(tutorial-env) -> pip show requests

# display all of the packages
(tutorial-env) -> pip list

# pip freeze will produce a similar list of the installed packages, but the output uses the format that pip install expects
(tutorial-env) -> pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)

# The requirements.txt can then be committed to version control and shipped as part of an application.
# Users can then install all the necessary packages with install -r:
-> pip install -r requirements.txt
```

# 13. What Now?

1. The Python Standard Library

2. Installing Python Modules 

3. The Python Language Reference

* http://code.activestate.com/recipes/langs/python/

# 14. Interactive Input Editing and History Substitution

* 14.1. Tab Completion and History Editing

* 14.2. Alternatives to the Interactive Interpreter

# 15. Floating Point Arithmetic: Issues and Limitations

* using the decimal module which implements decimal arithmetic suitable for accounting applications and high-precision applications

* Another form of exact arithmetic is supported by the fractions module which implements arithmetic based on rational numbers (so the numbers like 1/3 can be represented exactly).

* The float.as_integer_ratio() method expresses the value of a float as a fraction

* almost all platforms map Python floats to IEEE-754 “double precision”. 

# 16. Appendix

### 16.1.1. Error Handling

try...catch...

Typing the interrupt character (usually Control-C or Delete) 

### 16.1.2. Executable Python Scripts

```
#!/usr/bin/env python3.4
```

# The Python Language Reference

# The Python Standard Library
