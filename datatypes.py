Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=10
type(a)
<class 'int'>
b=4.5
type(b)
<class 'float'>
c='code'
>>> type(c)
<class 'str'>
>>> c="codegnan"
>>> type(c)
<class 'str'>
>>> d='''python'''
>>> type(d)
<class 'str'>
>>> e=2j+5
>>> type(e)
<class 'complex'>
>>> j=true
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    j=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> 
>>> j=True
>>> type(j)
<class 'bool'>
>>> f=False
>>> type(f)
<class 'bool'>
