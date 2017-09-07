# Learning Python With LeetCode

* **List Sort**
```python
#sorted()方法不替换本身，有返回值
l=[2,5,3,5,3]
sorted(l)
Out[2]: [2, 3, 3, 5, 5]

#list.sort()方法替换本身，无返回值
l.sort()
l
Out[6]: [2, 3, 3, 5, 5]
```

* **List Slices**
```python
l
Out[16]: [2, 4, 3, 5, 3, 5]

l[::1]
Out[17]: [2, 4, 3, 5, 3, 5]

l[::2]
Out[18]: [2, 3, 3]

l[::3]
Out[19]: [2, 5]

l[1:-1:2]
Out[20]: [4, 5]
```
**关于更多List**：https://developers.google.com/edu/python/lists


* **Sum**

Documentation: sum(iterable[, start])
即sum(,start),start默认为0，也可设为2、[]...
```python
sum((1,2))
Out[52]: 3

sum((1,2),3)
Out[53]: 6

num
Out[56]: [[1, 2], [3, 4]]

sum(num,[])
Out[57]: [1, 2, 3, 4]
#意味着[]+[1,2]+[3,4]
```


* **iter()**

```python
# list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

vowelsIter = iter(vowels)

# prints 'a'
print(next(vowelsIter))

# prints 'e'
print(next(vowelsIter))

# prints 'i'
print(next(vowelsIter))

# prints 'o'
print(next(vowelsIter))

# prints 'u'
print(next(vowelsIter))
```


* **zip()**
The syntax of zip() is:
```python
zip(*iterables)
```


* **zip(*[iter(s)]*n)**

iter(s) returns an iterator for s.

[iter(s)]*n makes a list of n times the same iterator for s.
```python
[iter(l)]*3
Out[80]: 
[<listiterator at 0xbad4b38>,
 <listiterator at 0xbad4b38>,
 <listiterator at 0xbad4b38>]
 ```
So, when doing zip(*[iter(s)]*n), it **extracts an item from all the three iterators from the list in order**. Since all the iterators are the same object, it just groups the list in chunks of n.


