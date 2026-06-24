Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a,b,c=2,3,4
print(a,b,c)
2 3 4
a,b,c=2,3,4,5,6,77
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a,b,c=2,3,4,5,6,77
ValueError: too many values to unpack (expected 3, got 6)
a,b,c=(3,4,5)
print(a,b,c)
3 4 5
first name="sudharshan"
SyntaxError: invalid syntax
first_name="sudharshan"
print(first_name)
sudharshan
firstname="sudharshan"
print(firstname)
sudharshan
>>> fname="sudharshan"
>>> 1name="madasu"
SyntaxError: invalid decimal literal
>>> print(fname+" "+1name)
SyntaxError: invalid decimal literal
>>> name="sudharshan"
>>> print(name)
sudharshan
>>> NAME="sudharshan"
>>> print(NAME)
sudharshan
>>> Name="sudhrshan"
>>> print(Name)
sudhrshan
>>> a=4
>>> print(a)
4
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
