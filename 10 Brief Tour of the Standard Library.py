# 10.1. Operating System Interface
import os
print(os.getcwd())

print(dir(os)) # <returns a list of all module functions>
print(help(os)) # <returns an extensive manual page created from the module's docstrings>

# 10.2. File Wildcards
import glob
# The glob module provides a function for making file lists from directory wildcard searches
print(glob.glob('*.py'))

# 10.3. Command Line Arguments
import sys
print(sys.argv)

# 10.4. Error Output Redirection and Program Termination
# The sys module also has attributes for stdin, stdout, and stderr
sys.stderr.write('Warning, log file not found starting a new one\n')

# 10.5. String Pattern Matching
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))

print('tea for too'.replace('too', 'two'))

# 10.6. Mathematics
import math
print(math.cos(math.pi / 4))
print(math.log(1024, 2))

import random
print(random.choice(['apple', 'pear', 'banana']))
print(random.sample(range(100), 10))
print(random.random())
print(random.randrange(6))

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.variance(data))
# The SciPy project <http://scipy.org> has many other modules for numerical computations

# 10.7. Internet Access
# from urllib.request import urlopen
# with urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl') as response:
#     for line in response:
#         line = line.decode('utf-8')  # Decoding the binary data to text.
#         if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#             print(line)

# Nov. 25, 09:43:32 PM EST

import smtplib
# example needs a mailserver running on localhost
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
#
# Beware the Ides of March.
# """)
# server.quit()

# 10.8. Dates and Times
from datetime import date
now = date.today()
print("now:", now)
print("now.strftime", now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

birthday = date(1987, 3, 25)
age = now - birthday
print(age.days)

left = date(2016,7,21) - now
print(left)

# 10.9. Data Compression
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))

t = zlib.compress(s)
print(len(t))

zlib.decompress(t)

print(zlib.crc32(s))

# 10.10. Performance Measurement
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())
# In contrast to timeit‘s fine level of granularity,
# the profile and pstats modules provide tools
# for identifying time critical sections in larger blocks of code

# 10.11. Quality Control
# One approach for developing high quality software is to
# write tests for each function as it is developed
# and to run those tests frequently during the development process
# The doctest module provides a tool
# for scanning a module
# and validating tests embedded in a program’s docstrings
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests

import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

unittest.main() # Calling from the command line invokes all tests

# 10.12. Batteries Included
# The xmlrpc.client and xmlrpc.server modules
# The email package is a library for managing email messages
# The json package
# The sqlite3 module
