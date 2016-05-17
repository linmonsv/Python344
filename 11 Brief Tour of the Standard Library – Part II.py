
# 11.1. Output Formatting
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))

import locale
print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True))

# 11.2. Templating
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
class BatchRename(Template):
    delimiter = '%'
fmt = 'Ashley_%n%f'#input('Enter rename style (%d-date %n-seqnum %f-format):  ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))

# 11.3. Working with Binary Data Record Layouts
# this example maybe error ?
import struct
"""
with open('MyTestSplit.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(3):                      # show the first 3 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size     # skip to the next header
"""
# 11.4. Multi-threading
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')

# 11.5. Logging
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')

# 11.6. Weak References
# The weakref module provides tools for tracking objects without creating a reference.
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive

del a                       # remove the one reference
gc.collect()                # run garbage collection right away

#d['primary']                # entry was automatically removed

# 11.7. Tools for Working with Lists
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])
# the result is array('H', [10, 700])

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)

from heapq import heapify, heappop, heappush
data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
print([heappop(data) for i in range(3)])  # fetch the three smallest entries

# 11.8. Decimal Floating Point Arithmetic
"""
financial applications and other uses which require exact decimal representation,
control over precision,
control over rounding to meet legal or regulatory requirements,
tracking of significant decimal places, or
applications where the user expects the results to match calculations done by hand.
"""
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))
print(round(.70 * 1.05, 2))
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)

getcontext().prec = 36
print(Decimal(1) / Decimal(7))
