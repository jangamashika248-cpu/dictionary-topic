Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dict{}
a={"name":"ashika","year":2026,"month":3}
print(a)
{'name': 'ashika', 'year': 2026, 'month': 3}
type(a)
<class 'dict'>
b={"name","year","month"}
type(b)
<class 'set'>
a.keys()
dict_keys(['name', 'year', 'month'])
a.values()
dict_values(['ashika', 2026, 3])
a.items()
dict_items([('name', 'ashika'), ('year', 2026), ('month', 3)])
#update()
a={"name":"ashika","city":"eluru","date":31}
a.update({"year":2026})
a
{'name': 'ashika', 'city': 'eluru', 'date': 31, 'year': 2026}
a.update({"month":3},{"time":10})
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.update({"month":3},{"time":10})
TypeError: update expected at most 1 argument, got 2
a.update({"month":3,"time":10})
a
{'name': 'ashika', 'city': 'eluru', 'date': 31, 'year': 2026, 'month': 3, 'time': 10}
#setdefault()
a={"mailid":"ashika@gmail.com"}
a.setdefault("name","ashika")
'ashika'
a
{'mailid': 'ashika@gmail.com', 'name': 'ashika'}
#pop()
a.pop()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("name")
'ashika'
a
{'mailid': 'ashika@gmail.com'}
a.pop("ashika@gmail.com")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a.pop("ashika@gmail.com")
KeyError: 'ashika@gmail.com'
a.copy()
{'mailid': 'ashika@gmail.com'}
a.clear()
>>> a
{}
>>> b.update({"day":"tuesday"})
>>> a
{}
>>> b.update({"day":"tuesday"})
>>> b
{'month', 'day', 'year', 'name'}
>>> #get()
>>> a={"city":"vij","country":"india"}
>>> a.get("country")
'india'
>>> a
{'city': 'vij', 'country': 'india'}
>>> a["city"]
'vij'
>>> a.popitem()
('country', 'india')
>>> a
{'city': 'vij'}
>>> a={"idnos":[10,20,30],"names":["ashika","kavya","ramya"]}
>>> print(a)
{'idnos': [10, 20, 30], 'names': ['ashika', 'kavya', 'ramya']}
>>> type(a)
<class 'dict'>
>>> a.keys()
dict_keys(['idnos', 'names'])
>>> a.values()
dict_values([[10, 20, 30], ['ashika', 'kavya', 'ramya']])
>>> a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['ashika', 'kavya', 'ramya'])])
>>> #duplicate
>>> a={"name":"ashika","city":"eluru","name":"ashika"}
>>> print(a)
{'name': 'ashika', 'city': 'eluru'}
>>> a={"name":"ashika","city":"eluru","name":"ashi"}
>>> print(a)
{'name': 'ashi', 'city': 'eluru'}
>>> a={"name":"ashika","city":"eluru","name1":"ashika"}
>>> print(a)
{'name': 'ashika', 'city': 'eluru', 'name1': 'ashika'}
