Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#striding
a="data science"
a[::]
'data science'
a[::1]
'data science'
a[::2]
'dt cec'
a[::4]
'd e'
a[::5]
'dsc'
a[::3]
'dacn'
a[2:3:5]
't'
a="cloud computing"
a[::5]
'c u'
a[::4]
'cdmi'
a[::8]
'cm'
a[2:]
'oud computing'
>>> a=[:9]
SyntaxError: invalid syntax
>>> a[:9]
'cloud com'
>>> a[3:11]
'ud compu'
>>> b="machine learing"
>>> b[3:14:2]
'hn ern'
>>> b[5:15:4]
'nen'
>>> b[2:12:3]
'cnlr'
>>> b[0:10:1]
'machine le'
>>> #negative striding
>>> a="python coures"
>>> a[-1:-10:-2]
'sro o'
>>> a[-5:-11:-3]
'on'
>>> a[-3:-13:-4]
'r t'
