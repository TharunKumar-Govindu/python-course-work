# #Recursive : A recursive function is a function that calls itself.
# Recursion continues until a stopping condition (Base Case) is reached.
'''
def fun(arg):
    if base:
        return
    fun(up arg)
fun()

'''

def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)

def display(n):
    if n==0:
        return
    print(n)
    display(n-1)
display(10)


def display(s,n):
    if n==len(s):
        return
    print(s[n])
    display(s,n+1)
display("Codegnan",0)