
a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x'))

a.insert(2, -1)
a.append(333)
print(a)

print(a.index(333))

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)

# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list
a.pop()
print(a)

# 5.1.1. Using Lists as Stacks
stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

print(stack.pop())
print(stack)

print(stack.pop())
print(stack.pop())

print(stack)

# 5.1.2. Using Lists as Queues
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue.popleft())                 # The first to arrive now leaves

print(queue.popleft())                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival

# 5.1.3. List Comprehensions
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x, y))
print(combs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])
# create a list of 2-tuples like (number, square)
print([(x, x**2) for x in range(6)])
# the tuple must be parenthesized, otherwise an error is raised

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

# 5.1.4. Nested List Comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print(matrix)

print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

print(list(zip(*matrix)))

# 5.2. The del statement
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
# del can also be used to delete entire variables
del a

# 5.3. Tuples and Sequences
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)
# Tuples are immutable:
# t[0] = 88888 will be error
v = ([1, 2, 3], [3, 2, 1])
print(v)

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(singleton))
print(singleton)

# 5.4. Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
# unique letters in a
print(a)
print(b)
print(a-b)
print(a|b)
print(a&b)
# letters in a or b but not both
print(a^b)

# 5.5. Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])
del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel.keys()))
print(sorted(tel.keys()))
print('guido' in tel)
print('jack' not in tel)

print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print({x: x**2 for x in (2, 4, 6)})

# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
print(dict(sape=4139, guido=4127, jack=4098))

# 5.6. Looping Techniques
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

# 5.7. More on Conditions
# Comparisons can be chained. For example, a < b == c tests whether a is less than b and moreover b equals c.

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2  or string3
print(non_null)

# 5.8. Comparing Sequences and Other Types




