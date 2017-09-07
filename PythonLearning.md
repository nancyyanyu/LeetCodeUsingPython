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
zip(*) - join the nth items of each list together
```python
>>> my_list=[[1,2,3],[4,5,6],[7,8,9,10]]
>>> print zip(*my_list)
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```


* zip(*[iter(s)]*n)

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



* **map( function, list, ...)**

**Apply function to every item of list and return a list of the results.** If additional list arguments are passed, function must take that many arguments and is applied to the items of all lists in parallel; **if a list is shorter than another it is assumed to be extended with None items.** If function is None, the identity function is assumed; if there are multiple list arguments, map() returns a list consisting of **tuples** containing the corresponding items from all lists (a kind of transpose operation). The list arguments may be any kind of sequence; the result is always a list.

```python
>>> my_list=[[1,2,3],[4,5,6],[7,8,9,10]]
>>> print map(None,*my_list)
[(1, 4, 7), (2, 5, 8), (3, 6, 9), (None, None, 10)]
```

*:"Arbitrary Argument List" and it's useful here as it expands our list to pass each of the lists within the outer list as an arguments to zip and map.


