Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#arthematic operator
a=4
b=5
print(a+b)
9
print(a-b)
-1
print(a*b)
20
print(a//b)
0
print(a/b)
0.8
print(a**b)
1024
print(a%b)
4
#assinment
a=3
b=5
print(a+=b)
SyntaxError: invalid syntax
a+b
8
a+=b
a
8
print(a)
8
a-=4
a
4
print(b+a)
9
b+=a
b
9
print(b)
9
b-=4
b
5
#comparision
a=4
b=9
a<b
True
b>a
True
a>b
False
b<a
False
a!=b
True
a==b
False
a<=b
True
b>=a
True
b<=a
False
a>=b
False
#logical
a=3
b=6
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b and b>a
True
a<b or b>a
True
a!=b or a==b
True
not True
False
not False
True
#identity operator
a=4
type(a)
<class 'int'>
>>> type(a) is int
True
>>> type(a)is not int
False
>>> b=6.7
>>> type(b) is float
True
>>> type(b) is not float
False
>>> c="pandu"
>>> type(c) is 'str'
False
>>> type(c) is not 'str'
True
>>> #membership operator
>>> a=2,3,4,5,6,7,8
>>> 8 in a
True
>>> 80 in a
False
>>> 80 not in a
True
