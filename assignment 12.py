1.
sum all the items in a dictionary
In [1]:
def Sum(myDict): 
      
    sum = 0
    for i in myDict: 
        sum+= myDict[i] 
    return sum
dict = {'a': 100, 'b':200, 'c':300} 
print("Sum :",Sum(dict))
Sum : 600

2.
Accessing an elements from a dictionary
In [4]:
d={'a':2,'b':4,'c':5,'d':8,'e':9}
print(d['c'])
print(d)
d['e']=4
print(d)
print(d.pop('d'))
print(d)
5
{'a': 2, 'b': 4, 'c': 5, 'd': 8, 'e': 9}
{'a': 2, 'b': 4, 'c': 5, 'd': 8, 'e': 4}
8
{'a': 2, 'b': 4, 'c': 5, 'e': 4}

3.
Concate two dictionaries
In [6]:
d1={'a':2,'b':4}
d2={'c':5,'d':8,'e':9}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)
Concatenated dictionary is:
{'a': 2, 'b': 4, 'c': 5, 'd': 8, 'e': 9}

4.
Add keys/values in a dictionary
In [8]:
print(d)
d['g']=0
d['r']='a'
print(d)
{'a': 2, 'b': 4, 'c': 5, 'e': 4}
{'a': 2, 'b': 4, 'c': 5, 'e': 4, 'g': 0, 'r': 'a'}

5.
The length of the dictionary
In [7]:
print(len(d))
4

6.
Remove items in the dictionary
In [9]:
print(d)
d.pop('g')
print(d)
{'a': 2, 'b': 4, 'c': 5, 'e': 4, 'g': 0, 'r': 'a'}
{'a': 2, 'b': 4, 'c': 5, 'e': 4, 'r': 'a'}