Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatype coversions
#int
int(6)
6
int(5.6)
5
int("python")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("python")
ValueError: invalid literal for int() with base 10: 'python'
int(3+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(3+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(2.4+5j)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    float(2.4+5j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
float(20000)
20000.0
str('True')
'True'
str('False')
'False'
str(2+4j)
'(2+4j)'
str(2)
'2'
complex(4)
(4+0j)
complex(2)
(2+0j)
complex(True)
(1+0j)
>>> complex(False)
0j
>>> complex('True')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    complex('True')
ValueError: complex() arg is a malformed string
>>> complex(2.3)
(2.3+0j)
>>> #bool
>>> bool(5.6)
True
>>> bool("hi")
True
>>> bool(6+3j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> bool(1)
True
