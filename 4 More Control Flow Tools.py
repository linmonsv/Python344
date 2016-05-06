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
