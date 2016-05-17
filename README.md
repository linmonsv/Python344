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
