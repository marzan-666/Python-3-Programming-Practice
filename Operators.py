Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x**2
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x**2
NameError: name 'x' is not defined
>>> # variable should be defined first
>>> x=2
>>> x**2
4
>>> x,y = 4,5
>>> x
4
>>> y
5
>>> #simultaneous assignment of variables
>>> 50/0 # numbers cant be divided by 0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    50/0 # numbers cant be divided by 0
ZeroDivisionError: division by zero
>>> 9/2
4.5
>>> 9%2
1
>>> 5+10*2
25
>>> (6+7)*2
26
>>> 