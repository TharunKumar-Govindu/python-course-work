import sys 

print(sys.version)
print(sys.argv)
print(sys.path)
print("Start of the program")
print(sys.exit())   
print("End of the program")

import platform
print(platform.system())
print(platform.release())
print(platform.version())
print(platform.processor())


import math 
print(math.pi)
print(math.e)
print(math.sqrt(16))
print(math.factorial(5))
print(math.pow(2, 3))
print(math.ceil(2.3))
print(math.floor(2.7))  
print(math.sin(30))
print(math.cos(60))
print(math.tan(45))


import random
random.seed(10)
print(random.random())
print(random.randint(999999, 10000000))
print(random.uniform(1, 10))

l = [1, 2, 3, 4, 5]
print(random.choice(l))

lang = ['Python', 'Java', 'C++', 'JavaScript']
print(random.choice(lang))


from collections import Counter


s = 'kadali nikhil sai kumar'
res = Counter(s)
print(res)


from collections import Counter,defaultdict

products = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
res = defaultdict(list)

for i in products:
    res[i].append('dev', 'rev')

print(res)

s= 'python prrogramming'
d = defaultdict(int)
for i in s:
    d[i]+=1
print(d)


from collections import deque
l =deque([])

l.append(1)
l.append(2) 
l.appendleft(3)
l.appendleft(4)

l.popleft() 
l.pop()    

print(l)

