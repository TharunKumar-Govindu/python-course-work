#local variable:The variable which is declear inside the function
#Global Variable: The variable which is declear outside the function

def display():
    n=10
    print("Inside the function:",n)
    
display()
print("Outside the function:",n)


#global keyword make local variable to both inside and outside of the function


def display():
    global n
    n=10
    print("Inside the function:",n)
    
display()
print("Outside the function:",n)


#we are not suppose to pass global variable as parameters 

def display():
        global n
        n=10
        print("Inside the function:",n)
    
display()
print("Outside the function:",n)



def display():
    course = 'PFS'
    def update():
        nonlocal course
        course = 'JFS'
        print("Inner Function",course)
    update()
    print("Outer Function",course)

display()


l = [1,3,4,5]
print(max(l))

print = 20
print(print)

