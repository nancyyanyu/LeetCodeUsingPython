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

```python
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zipped)
>>> x == list(x2) and y == list(y2)
True
```

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



* **Difference of zip() and zip(*list)**

```python
my_list=[[1,2,3],[4,5,6],[7,8,9,10]]

zip(my_list)
Out[84]: [([1, 2, 3],), ([4, 5, 6],), ([7, 8, 9, 10],)]

zip([1,2,3],[4,5,6],[7,8,9])
Out[85]: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

zip wants a bunch of arguments to zip together, but what you have is a single argument (a list, whose elements are also lists). The * in a function call "unpacks" a list (or other iterable), making each of its elements a separate argument. So without the *, you're doing zip( [[1,2,3],[4,5,6]] ). With the *, you're doing zip([1,2,3], [4,5,6]).



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

iter() is an iterator over a sequence. [x] * n produces a list containing n quantity of x, i.e. a list of length n, where each element is x. *arg unpacks a sequence into arguments for a function call. Therefore you're passing the same iterator 3 times to zip(), and it pulls an item from the iterator each time.



* **map( function, list, ...)**

**Apply function to every item of list and return a list of the results.** If additional list arguments are passed, function must take that many arguments and is applied to the items of all lists in parallel; **if a list is shorter than another it is assumed to be extended with None items.** If function is None, the identity function is assumed; if there are multiple list arguments, map() returns a list consisting of **tuples** containing the corresponding items from all lists (a kind of transpose operation). The list arguments may be any kind of sequence; the result is always a list.

```python
>>> my_list=[[1,2,3],[4,5,6],[7,8,9,10]]
>>> print map(None,*my_list)
[(1, 4, 7), (2, 5, 8), (3, 6, 9), (None, None, 10)]
```

*:"Arbitrary Argument List" and it's useful here as it expands our list to pass each of the lists within the outer list as an arguments to zip and map.


* **remove() & del**

list.remove(obj)和del list[i]都无返回值

```python
l=[2,3,4,6,3,7]

l.remove(3)

l
Out[151]: [2, 4, 6, 3, 7]

l.remove(l[2])

l
Out[153]: [2, 4, 3, 7]

del l[-1]

l
Out[155]: [2, 4, 3]
```


* **count()**

```python
l=[1,2,3,4,2,2,2,4]

l.count(2)
Out[158]: 4
```


