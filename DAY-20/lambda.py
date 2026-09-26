'''
syntax: 

var = lambda arg: expression
'''
wish = lambda name: f"Hello {name}, Good Morning!"
print(wish("prasad"))
print(wish("nikhil"))


gst = lambda price: price + price * 0.18
print(gst(1000))
print(gst(5000))


avg = lambda a, b ,c : (a + b + c) / 3
print(avg(10, 20, 30))
print(avg(12,14,54))


iseven = lambda a: "Even" if a % 2 == 0 else "Odd"
print(iseven(10))
print(iseven(15))


largest = lambda a, b, c: a if a>b and a>c else (b if b>c else c)
print(largest(10, 20, 12))
print(largest(30, 12, 25))

isvowel = lambda a: "Vowel" if a in "aeiouAEIOU" else "Consonant"
print(isvowel("a")) 
print(isvowel("b"))


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
update = list(map(lambda i: i+10, l))
print(update)


t = (789,123,456,743,120)
discount = list(map(lambda i : i - i*0.3, t))
print(discount)


l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
update = list(filter(lambda i: i%2!=0, l))
print(update)

t = (789,123,456,743,120,78,54)
update = list(filter(lambda i : i>100, t))
print(update)


l=['tharun@codegnan.com','tharun@gmail.com','tharun@yahoo.com']
update = list(map(lambda i: i.split('@')[1], l))
print(update)   


from functools import reduce
l = [12,123,31,4332,4]
res =reduce(lambda sum,i: sum+i, l)
print(res)

prod = reduce(lambda a,b: a*b, l)
print(prod)


seats = {'s1':True, 's2':False, 's3':True, 's4':False, 's5':True}
available_seats = list(filter(lambda seat: seats[seat]==False, seats))
print(available_seats)  

products = {'egg': 10, 'milk': 20, 'bread': 15, 'butter': 25, 'cheese': 30 }
products=list(filter(lambda i : products[i]>20, products))
print(products)


products = {'egg': 10, 
            'milk': 20,
              'bread': 15, 
              'butter': 25,
                'cheese': 30
                  }
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))
print(dict(sorted(products.items(),key=lambda i:i[1])))
