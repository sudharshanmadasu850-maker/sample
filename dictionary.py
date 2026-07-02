Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict{}
a={"name":"sudharshan","city":"vij"}
print(a)
{'name': 'sudharshan', 'city': 'vij'}
type(a)
<class 'dict'>
b ={3,4,5,6,7,"name"}
type(b)
<class 'set'>
a={"name":"sudharshan","mailid":"sudharshanmadasu850@gmail.com","mobileno":6300362138}
print(a)
{'name': 'sudharshan', 'mailid': 'sudharshanmadasu850@gmail.com', 'mobileno': 6300362138}
a.keys()
dict_keys(['name', 'mailid', 'mobileno'])
a.values()
dict_values(['sudharshan', 'sudharshanmadasu850@gmail.com', 6300362138])
a.items()
dict_items([('name', 'sudharshan'), ('mailid', 'sudharshanmadasu850@gmail.com'), ('mobileno', 6300362138)])
a={"coures":"python","institue":"codegnan"}
a.update({"name":"sudharshan"})
a
{'coures': 'python', 'institue': 'codegnan', 'name': 'sudharshan'}
a.update({"year":2026,"month":7})
a
{'coures': 'python', 'institue': 'codegnan', 'name': 'sudharshan', 'year': 2026, 'month': 7}
a={"year":2026,"month":"july"}
a.setdefault("date",3)
3
a
{'year': 2026, 'month': 'july', 'date': 3}
a={"time":12,"hour":1,"min":3}
a.pop("hour")
1
a.popitem()
('min', 3)
a
{'time': 12}
a
{'time': 12}
a={"college":"vignan","branch":"bsc"}
a.get("college")
'vignan'
a["branch"]
'bsc'
a
{'college': 'vignan', 'branch': 'bsc'}
a.get("bsc")
a
{'college': 'vignan', 'branch': 'bsc'}
>>> a={"hour":12,"min":2,"sec":60}
>>> a.copy()
{'hour': 12, 'min': 2, 'sec': 60}
>>> a
{'hour': 12, 'min': 2, 'sec': 60}
>>> a.clear()
>>> a
{}
>>> b={}
>>> b.update({"name":"sudharshan"})
>>> b
{'name': 'sudharshan'}
>>> a={"name":"sudharshan","course":"python","year":2026}
>>> len(a)
3
>>> a={"name":"sudharshan","city":"krosur","name":"sudharshan"}
>>> print(a)
{'name': 'sudharshan', 'city': 'krosur'}
>>> a={"name1":"sudharshan","city":"krosur","name2":"sudharshan"}
>>> print(a)
{'name1': 'sudharshan', 'city': 'krosur', 'name2': 'sudharshan'}
>>> a={"idnos":[20,30,40],"names":["sai","karthik","deva"],"marks"[40,50,80]}
SyntaxError: ':' expected after dictionary key
