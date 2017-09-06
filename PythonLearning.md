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

