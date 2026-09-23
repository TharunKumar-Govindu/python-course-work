Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python operators
>>> #arithmetic operator
>>> a=10
>>> b=20
>>> a+b
30
>>> a-b
-10
>>> a*b
200
>>> a/b
0.5
>>> a**b
100000000000000000000
>>> a//b
0
>>> a%b
10
>>> 12//12
1
>>> 12//3
4
>>> #comparison operator
>>> a=13
>>> b=17
>>> a>b
False
>>> a<b
True
>>> a>=b
False
>>> a<=b
True
>>> a==b
False
>>> a!=b
True
>>> #assignment operators
>>> a=12
>>> a+=15
>>> a
27
>>> a-=7
>>> a
20
>>> a**=2
>>> a
400
>>> a/=2
>>> a
200.0
>>> a%=2
>>> a
0.0
>>> a
0.0
>>> a=12
>>> a
12
>>> a+=12.12
>>> a
24.119999999999997
>>> a%=2
>>> a
0.11999999999999744
>>> =2
SyntaxError: invalid syntax
>>> a=12
>>> a
12
>>> #relational operators
>>> email = True
>>> password = False
>>> email and password
False
>>> 's' in 'aeiou'
False
>>> 't' not in 'aeiou'
True
>>> 3%2==0
False
>>> 4%2==0
True
>>> #membership operator
>>> #works with only string list tuple set dict
>>> name = 'Tharun'
>>> 't' in name
False
>>> 'a' in name
True
>>> 's' not in name
True
>>> l = [1,2,3,4]
>>> a in l
False
>>> 4
4
>>> 4 in l
True
>>> 5 in l
False
>>> 7 not in l
True
>>> t = (9,8,7,6,5)
>>> 3 in t
False
>>> 6 in t
True
>>> 8 in t
True
>>> 8 not in t
False
>>> s ={1,2,3,4,5}
>>> 5 in s
True
>>> 7 not in s
True
>>> 11 in s
False
>>> d = {'a':1,'b':2,'c':3,'d':4,'e':5}
>>> #in dict works only for keys
>>> 1 in d
False
>>> 'a' in d
True
>>> 'd' in d
True
>>> 3 not in d
True
>>> #bitwise operators
>>> 15 &16
0
>>> 2 & 3
2
>>> 3 & 2
2
>>> 1 & 2
0
>>> 12 | 13
13
>>> 14|15
15
>>> 1^3
2
>>> ~4
-5
>>> ~5
-6
>>> 2<<4
32
>>> 4<<6
256
>>> 2<<3
16
>>> 4>>6
0
>>> 6>>2
1
>>> #logical operators
>>> 1 and 2
2
>>> 12 and 13
13
>>> 123 or 54
123
>>> 87 or 63
87
>>> 63 or 87
63
>>> #identity operators
>>> a=[1,2,3,4]
>>> b= [1,2,3,4]
>>> a==b
True
>>> id(a)
1307227330816
>>> id(b)
1307219930688
>>> a in b
False
>>> b in a
False
>>> c=a
>>> c
[1, 2, 3, 4]
>>> id (c)
1307227330816
>>> id (a)
1307227330816
>>> a in c
False
>>> c in a
False
>>> 
