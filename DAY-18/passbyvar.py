#int float complex str list tuple set dict bool
#int

def display(n):
    n+=6
    print("Inside the function:",n)
n =21 
display(n)
print("Outside function:",n)


#float
def display(n):
    n+=6.7
    print("Inside the function:",n)
n =21.3
display(n)
print("Outside function:",n)


#complex
def display(n):
    n=6
    print("Inside the function:",n)
n =21+4j
display(n)
print("Outside function:",n)

#string
def display(n):
    n += 'kumar'
    print("Inside the function:",n)
n = 'tharun'
display(n)
print("Outside function:",n)

#list
def display(n):
    n.append(10)
    print("Inside the function:",n)
    n =[1,2,3,4]
display(n)
print("Outside function:",n)



def display(n):
    n.update(12)
    print("Inside the function:",n)
n =(1,2,3,4)
display(n)
print("Outside function:",n)


