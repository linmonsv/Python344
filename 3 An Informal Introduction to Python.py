# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

# 3.1. Using Python as a Calculator
# >>> 2 + 2

# >>> 2 ** 7  # 2 to the power of 7
# 128

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

text = ('Put several strings within parentheses '
            'to have them joined together.')
print(text)

# Strings can be indexed
# >>> word = 'Python'
# >>> word[0]  # character in position 0
# 'P'
# >>> word[0:2]  # characters from position 0 (included) to 2 (excluded)
# 'Py'

squares = [1, 4, 9, 16, 25]
print(squares)
squares.append(216)
print(squares)
print(len(squares))

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

