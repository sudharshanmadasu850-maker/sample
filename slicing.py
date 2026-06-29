Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a="codegnan"
a[0]+a[1]+a[2]+a[3]
'code'
#slicing
a[0:3]
'cod'
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
b="until you work succeed"
b[0:4]
'unti'
b[0:5]
'until'
b[5:8]
' yo'
b[8:11]
'u w'
b[5:10]
' you '
c="codegnan it solutions"
>>> c=[9:11]
SyntaxError: invalid syntax
>>> c=[0:4]
SyntaxError: invalid syntax
>>> #negitive slicing
>>> d="vijayawada is aroyal city"
>>> d[-10:-5]
'royal'
>>> d[-24:-16]
'ijayawad'
>>> d[-25:-16]
'vijayawad'
>>> d[-25:-17]
'vijayawa'
>>> d[-4:]
'city'
>>> e="vizag is the city of destiny"
>>> e[-15:-11]
'city'
>>> e[-24:-19]
'g is '
>>> e[-17:]
'e city of destiny'
