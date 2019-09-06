# python operators
# + ---> addition
# - ---> subtraction
# / ---> division
# * ---> mutiplication
# % ---> modulus
# ** --=> exponent


x = 5%3 #modulus return remainder after divition
print("modulus :", x)

x = 5/3 #normal divition return a float with decimal value 
print("normal division :", x)

x = 5//3 #floor divition return a integer rounded down 
print("floor division  :", x)

x = 5 ** 3 #exponent raises to power
print("exponent operation  :", x)

# assignment operators
# = ---> basic assignment
# += ---> addition & assign
# -= ---> subtraction & assign

print("\n\nAT BASIC ASSIGNMENT")
apple = 6 #basic asignment, assign variables
print("APPLES : ", apple)

print("\n\nAT subtract and assignment\n".upper())

apple -= 1 #subtract and assign varriable
print("APPLES : ", apple)
apple -= 1 #subtract and assign varriable
print("APPLES : ", apple)
apple -= 1 #subtract and assign varriable
print("APPLES : ", apple)
apple -= 1 #subtract and assign varriable
print("APPLES : ", apple)
apple -= 1 #subtract and assign varriable
print("APPLES : ", apple)
apple -= 1 #subtract and assign varriable
print("APPLES : ", apple)

print("\n\nAT addtion and assignment\n".upper())

apple += 1 #addition and assign varriable
print("APPLES : ", apple)
apple += 1 #addition and assign varriable
print("APPLES : ", apple)
apple += 1 #addition and assign varriable
print("APPLES : ", apple)
apple += 1 #addition and assign varriable
print("APPLES : ", apple)
apple += 1 #addition and assign varriable
print("APPLES : ", apple)
apple += 1 #addition and assign varriable
print("APPLES : ", apple)

print("\n\nAT multipliction and assignment\n".upper())

apple *= 2 #multiplication and assign varriable
print("APPLES : ", apple)
apple *= 2 #multiplication and assign varriable
print("APPLES : ", apple)
apple *= 2 #multiplication and assign varriable
print("APPLES : ", apple)
apple *= 2 #multiplication and assign varriable
print("APPLES : ", apple)
apple *= 2 #multiplication and assign varriable
print("APPLES : ", apple)
apple *= 2 #multiplication and assign varriable
print("APPLES : ", apple)

print("\nlogical operators".upper())
t = True
f = False
print("\nfor and operation".upper())
print(t and t)#should print true
print(t and f)#should print false
print(f and t)#should print false
print(f and f)#should print false

print("\nfor or operation".upper())
print(t or t)#should print true
print(t or f)#should print true
print(f or t)#should print true
print(f or f)#should print false

print("\nfor in operation\n".upper())
name = "adebayo"

print("x" in name, "before adding the NOT logical operator")#should print false character 'x' is not a member of name
print("a" in name)
print("x" not in name)

print("\nmixing membership operation with the logical operation for multiple teast".upper())

test_list = [1,4,5,6,7,8]

print(1 in test_list,", single test")
print(1 in test_list and 32 in test_list,", mutiple tests with 'AND' logical operator")
print(1 in test_list and 32 not in test_list,", mutiple tests with 'AND' logical operator and 'NOT' inverting factor")

print(1 in test_list and 32 not in test_list or 8 in test_list,", mutiple tests with 'AND' $ 'NOT' logical operator and 'NOT' inverting factor")

print(1 in test_list and 32 in test_list or 8 not in test_list,", mutiple tests with 'AND' logical operator and 'NOT' inverting factor\n")

print("\nidentity operator\n".upper())

x = 20
y = 30 

print(x is y)

x = y 
print(x is y)

print("\ncomparision operator\n".upper())

a = 23
b = 32
c = 23
boy = "adamu"
girl = "suliyat"
somebody = "adamu"

print(a == b, " >----> using the equal to(==) operator")
print(a != b, " >----> using the not equal to(!=) operator")
print(a == c, " >----> using the equal to(==) operator")
print(a != b, " >----> using the not equal to(!=) operator")

print(a > c, " >----> using the greater than to(>) operator")
print(a < c, " >----> using the less than to(<) operator")

print(a >= c, " >----> using the greater than equal to(>=) operator")
print(a <= c, " >----> using the less than equal to(<=) operator")

print(boy == girl, ">---> using the equal to (==) operator")
print(boy == somebody, ">---> using the equal to(==) operator")

print(len(boy), len(girl), len(somebody))

name = input("please what is your name: ")
print("my name is ", name)
print("the lenght of my name is:", len(name))


greeting = "hello world"
num1 = 2
num2 = 3
num3 = 4

print(greeting)

print(greeting, num1, num2, num3)
print(greeting, num1, num2, num3, sep = "---")
print(greeting, num1, num2, num3, sep = "---", end = "end")
print("this is another print statement")

# map built in function
unsorted = [1,6,0,9,32,3,4]
stringed_list = map(str, unsorted)
print("\n list string --->", list(stringed_list))

list_for_join = ['1', '6', '0', '9', '32', '3', '4']
joined = ";".join(list_for_join)
print("\n Joined List string --->", joined)

