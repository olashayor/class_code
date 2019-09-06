#a = 3
#b = 5
#c = (a**2 + b**2) **0.5
#print(c)
#a = input("please enter the value of adjacent : ")
# b = input("please enter the value of opposite : ")
# c = (int(a)**2 + int(b)**2) **0.5
# print("the hypotenous = ".upper(), c)

print("\nASSIGNMENT ")
x = input("what side of the triangle are u look for: a = adjacent, b = opposite, c = hypotenous  ".upper())
if x.lower() == "b":
    a = input("what is the value of the adjacent : ")
    c = input("what is the value of the hypotenous : ")
    b = (int(c)**2 - int(a)**2) **0.5
    print("the opposite of the triange = ".upper(), b)
elif x.lower() == "a":
    b = input("what is the value of the opposite : ")
    c = input("what is the value of the hypotenous : ")
    a = (int(c)**2 - int(b)**2) **0.5
    print("the adjacent of the triange = ".upper(), a)
elif x.lower() == "c":
    a = input("what is the value of adjacent : ")
    b = input("what is the value of opposite : ")
    c = (int(a)**2 + int(b)**2) **0.5
    print("the hypotenous of the triange = ".upper(), c)
else:
    print("this program is for solving the sides of a triangle using pythagoras theorem!".upper())

print("\n classwork ".upper())    
p = int(input("type any number to : ".upper()))
if p % 2 == 0:
    print("the number is an even number ".upper())
else:
    print("the number is an odd number ".upper())

