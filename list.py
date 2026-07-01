Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list
a=[2,5.6,"python",6+9j,True,False]
print(a)
[2, 5.6, 'python', (6+9j), True, False]
type(a)
<class 'list'>
b=5
type(b)
<class 'int'>
c=[5]
type(c)
<class 'list'>
a=["python","java","c","c++"]
a.append("DSA")
a
['python', 'java', 'c', 'c++', 'DSA']
a.append("aimi")
a
['python', 'java', 'c', 'c++', 'DSA', 'aimi']
#extend
a=["ml","ai","ds"]
a.extend(["c","c++","python"])
a
['ml', 'ai', 'ds', 'c', 'c++', 'python']
#insert
b=["vij","hyd"]
b.insert(2,"viz")
b
['vij', 'hyd', 'viz']
#index
a=["black","red","white","pink"]
a.index("red")
1
a.copy()
['black', 'red', 'white', 'pink']
b=a.copy()
b
['black', 'red', 'white', 'pink']
b.count("red")
1
#sort
a=["grapes","apple","mango","banana"]
a.sort()
a
['apple', 'banana', 'grapes', 'mango']
b=[3,5,4,6,7,1]
b.sort()
b
[1, 3, 4, 5, 6, 7]
#reverse()
a=[20,30,45,67,89]
a.reverse()
a
[89, 67, 45, 30, 20]
b=["python","java","css","c++"]
b.reverse()
b
['c++', 'css', 'java', 'python']
#pop()
a=["c","c++","java","python"]
a.pop()
'python'
a
['c', 'c++', 'java']
a.pop(2)
'java'
>>> a
['c', 'c++']
>>> #remove
>>> a.remove(2)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.remove(2)
ValueError: list.remove(x): x not in list
>>> a.remove("c")
>>> a
['c++']
>>> a=["gopi","deva","karthik","rk"]
>>> len(a)
4
>>> b="deva"
>>> len(b)
4
>>> c=["karthik"]
>>> len(c)
1
>>> a.clear()
>>> a
[]
