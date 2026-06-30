Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#strings methods
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
#count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("i")
3
a.count("k")
2
a.count("s")
1
#find a string
a="code"
a[1]
'o'
a.find("d")
2
a.find("e")
3
b="hello"
b.find("l")
2
#escape squences
#\n->new line
#\t->tab space
a="name\nmobile\tmailid\nclg
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobile\tmailid\nclg"
print(a)
name
mobile	mailid
clg
b="name:sudharshan\nmobile:6300362138\tmailid:sudharshanmadasu850@gmail.com\nclg:codegnan"
print(b)
name:sudharshan
mobile:6300362138	mailid:sudharshanmadasu850@gmail.com
clg:codegnan
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="work work until you succeed"
b.replace("work","wait",1)
'wait work until you succeed'
#upper
a="hello"
a.upper()
'HELLO'
#lower
b="HI"
b.lower()
'hi'
c="python"
c.captalize()
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    c.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
a="python course"
a.title()
'Python Course'
b="i am in class"
b.title()
'I Am In Class'
a="java"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
d="1234"
d.isdigit()
True
d.isalnum()
True
e="sudharshan12334"
e.isalnum()
True
a="hello python"
a.startswith("h")
True
a.endswith("n")
True
#strip()
#1strip(),rstrip()
a="        sudharshan      "
a.strip()
'sudharshan'
a.1strip()
SyntaxError: invalid decimal literal
a.lstrip()
'sudharshan      '
a.rstrip()
'        sudharshan'
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in krosur"
b.split()
['i', 'am', 'in', 'krosur']
c="codegnan"
c.split()
['codegnan']
#join
a="vij hyd vzg"
"".join(a)
'vij hyd vzg'
b="vij","hyd","vzg"
"".join(b)
'vijhydvzg'
#concatenation
a="hello"
b="world"
print(a+b)
helloworld
print(a+" "+b)
hello world
aname="sudharshan"
bname="madasu"
print(aname+bname)
sudharshanmadasu
print(aname+" "+bname)
sudharshan madasu
print(aname+" "+bname).title())
SyntaxError: unmatched ')'
print(aname+" "+bname).tittle())
SyntaxError: unmatched ')'
#formating
a=4
b=8
print(a+b)
12
print("the sum of",a+b)
the sum of 12
>>> x="vja"
>>> print("city is",x)
city is vja
>>> #format method
>>> a="motu"
>>> b="patlu"
>>> print("hello",a+b)
hello motupatlu
>>> print("hello {}{}".format(a,b))
hello motupatlu
>>> #fstring
>>> a="sita"
>>> b="ram"
>>> print(f"hello {a}{b}")
hello sitaram
>>> print(f"hello {a} {B}")
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    print(f"hello {a} {B}")

