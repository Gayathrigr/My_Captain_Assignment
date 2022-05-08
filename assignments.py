#Assignment 1
# 1. Implement Input and print function
x=input("Enter your name : ")
print("Hello ", x)

#2. Implement functions of string from w3schools

# capitalize()
x = "hello world."
y = x.capitalize()
print (y)

#casefold()
x = "Hello World!"
y = x.casefold()
print(y)

#center()
x= "banana"
y = x.center(20)
print(y)

#count()
x = "I love apples, apple are my favorite fruit"
y = x.count("apple")
print(x)

#encode()
x= "My name is Ståle"
y = x.encode()
print(y)

#endswith()
x = "Hello, welcome to my world."
y = x.endswith(".")
print(y)

#expandtabs()	
y = "H\te\tl\tl\to"
x =  y.expandtabs(2)
print(x)

#find()
y = "Hello, welcome to my world."
x = y.find("welcome")
print(x)

#format()
x = "For only {price:.2f} dollars!"
print(x.format(price = 49))

#format_map()
a = {'x':'John', 'y':'Wick'}
print("{x}'s last name is {y}".format_map(a))

#index()
y = "Hello, welcome to my world."
x = y.index("welcome")
print(x)

#isalnum()
y = "Company 12"
x = y.isalnum()
print(x)

#isalpha()
y = "Company10"
x = y.isalpha()
print(x)

#isdecimal()
y = "\u0033" #unicode for 3
x = y.isdecimal()
print(x)

#isdigit()
y = "50800"
x = y.isdigit()
print(x)

#isidentifier()
b = "Demo002"
print(b.isidentifier())

#islower()
y = "hello world!"
x = y.islower()
print(x)

#isnumeric()
y = "565543"
x = y.isnumeric()
print(x)

#isprintable()
y = "Hello! Are you #1?"
x = y.isprintable()
print(y)

#isspace()
y = "   s   "
x = y.isspace()
print(x)

#istitle()
y = "Hello, And Welcome To My World!"
x = y.istitle()
print(x)

#isupper()
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

#join()
y = ("John", "Peter", "Vicky")
x = "#".join(y)
print(x)

#ljust()
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

#lower()
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

#lstrip()
xt = "     banana     "
x = xt.lstrip()
print("of all fruits", x, "is my favorite")

#maketrans()
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

#partition()
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

#replace()
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#rfind()
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

#rindex()
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

#rjust()
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

#rpartition()
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

#rsplit()
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

#rstrip()
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

#split()
txt = "welcome to the jungle"
x = txt.split()
print(x)

#splitlines()
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

#startswith()
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

#strip()
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")

#swapcase()
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

#title()
txt = "Welcome to my world"
x = txt.title()
print(x)

#translate()
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#upper()
txt = "Hello my friends"
x = txt.upper()
print(x)

#zfill()
txt = "50"
x = txt.zfill(10)
print(x)



# Implement functions of list from w3schools

#append()
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
#clear()
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()

#copy()
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()

#count()
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")

#extend()
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)

#index()
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")

#insert()
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")

#pop()
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)

#remove()
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")

#reverse()
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

#sort()
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()



# Assignment 2

#1 w3school methods for dictionary data structure


#clear()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
car.clear()
print(car)

#copy()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
x = car.copy()
print(x)

# fromkeys()
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)


#get()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
x = car.get("model")
print(x)

#items()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
x = car.items()
print(x)


#keys()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
x = car.keys()
print(x)

#pop()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
x = car.pop("model")
print(x)

#popitems()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
car.popitem()
print(car)

#setdefault()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
x = car.setdefault("model", "Bronco")
print(x)

#update()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
car.update({"color": "White"})
print(car)


#values()
car = {"brand": "Ford","model": "Mustang","year": 1964 }
x = car.values()
print(x)



# 2.study sets in w3schools
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# methods........


# add() 
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

#clear()
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)

# copy() 
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)



# difference() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

#difference_update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

#discard()

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

#intersection() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#intersection_update() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#isdisjoint() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

#issubset() 
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# issuperset() 
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
# pop() 
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

#remove() 
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


#symmetric_difference() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

#symmetric_difference_update() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#union() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

#update()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)



