#x = int(input("Please enter an integer: "))
x = 5
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))
for w in words[:]:# Loop over a slice copy of the entire list.
    if len(w) > 6:
        words.insert(0, w)
print(words)

for i in range(5):
    print(i)
for i in range(5, 10):
    print(i)
for i in range(0, 10, 3):# ‘step’
    print(i)
for i in range(-10, -100, -30):
    print(i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

print(range(10)) # A strange thing happens

print(list(range(5)))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a number", num)

# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+C)

class MyEmptyClass: # This is commonly used for creating minimal classes
    pass

# a place-holder
def initlog(*args):
    pass   # Remember to implement this!

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)

fibf = fib
fibf(2000)

def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100)                # write the result

# 4.7.1. Default Argument Values
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise OSError('uncooperative user')
        print(complaint)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

i = 5

def f107(arg=i):
    print(arg)
# The default values are evaluated at the point of function definition in the defining scope,
# so that will print 5.
i = 6
f107()

# Important warning: The default value is evaluated only once
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))# [1]#
print(f(2))# [1, 2]#
print(f(3))# [1, 2, 3]#

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f2(1))# [1]
print(f2(2))# [2]
print(f2(3))# [3]

# Functions can also be called using keyword arguments of the form kwarg=value
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# but all the following calls would be invalid:
# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

print("When a final formal parameter of the form **name is present, it receives a dictionary ")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)

    for arg in arguments:
        print(arg)

    print("-" * 40)

    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger",

           "It's very runny, sir.",
           "It's really very, VERY runny, sir.",

           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def concat(*args, sep="/"):
    return sep.join(args)
print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))

# 4.7.4. Unpacking Argument Lists
print(list(range(3, 6))) # normal call with separate arguments
args = [3, 6]
# the built-in range() function expects separate start and stop arguments
print(list(range(*args))) # call with arguments unpacked from a list

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

# Small anonymous functions can be created with the lambda keyword
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

def f215(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f215('spam'))
