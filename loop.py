# for letter in "awele":
#       print(letter)

# for anything in "awele":
#         print(anything)

# word = "Microparamecium"
# print(word[2]) #string indexing

# for number in range(200):
#         print(number)

# for letter in "feyisayo":
#   print(letter)

# for number in range(20,40):     #to list from 20 to 39
#          print(number)

# for number in range(20,40,2):     #to list from 20 to 39 wth distance of two
#          print(number)

# for number in reversed(range(20,40)):     #to list from 39 to 20
#          print(number)

# word = "Microparamecium"
i = 0
# while i < 15:
#         print(word[1])
#         i += 1 

# while i <= 5:       #infite loop no stopping value
#         print(i)

# while i < 5:        #not infinte loop 
#         print(i)
#         i + 1        

# even number printting
# for i in range(0,100):
#     if i % 2 == 0: print(i)

# odd number printting
# for i in range(100):
#     if i % 2 != 0: print(i)

# count odd number
# odd_number = 0
# for i in range(100):
#         if i % 2 != 0:
#                 print(i)
#                 odd_number += 1

# print(f"the total odd number is {odd_number}")

# count even and odd number
# odd_number = 0
# even_number = 0

# for i in range(100):
#         even_number += 1
#         if i % 2 != 0:
#                 print(i)
#                 odd_number += 1
#                 even_number -= 1

# print(f"the total odd number is {odd_number}")
# print(f"the total odd number is {even_number}")
#         # OR
# count even and odd number
# odd_number = 0
# even_number = 0

# for i in range(100):
#         if i % 2 != 0:
#                 print(i)
#                 odd_number += 1         #increase odd number
#         else:
#                 even_number += 1        #increase even number

# print(f"the total odd number is {odd_number}")
# print(f"the total odd number is {even_number}")

# i = 0
# while True:
#         num1 = int(input("please enter a number : "))
#         num2 = int(input("please enter another number : "))
#         print(f"sum is {num1 + num2}")
 
# price = [3, 0, 6, 7, 8, 3, 6]
# total = 0
# for price in price:
#         total += price
# print(f"Total: {total}")

# for x in range(4):
#         for y in range(4):
#                 print(f"({x}  {y})")


# NUMBER GUESSING GAME
import random           # to make the computer generate a random number
number = random.randint(1, 100)
print("\nI am thinking of a number between 1 and 100".upper())
print("\ntry if you can get the number".upper())
trial = 0
while True:
        guess = int(input("enter a number between 1 and 100 : "))
        trial += 1      #to make the trial increase as the input does
        if guess > number and guess < 101:
                print("your number is greater than mine")

        elif guess < number and guess < 101:
                print("your number is less than mine")

        elif guess == number:
                print("GREAT!!! You are correct")
                break

        else:
                print("your number to guess is between 1 and 100")

print(f"you get the correct answer after {trial} attempt".upper())
if trial <= 5:
        print("that is a good attempt".upper())
else:
        print("that is not a good attempt".upper())



# import math
# print( """x + x + x = z
#           y + y + y = z
#           z + z + z = z""")


# assignment (exhaustive enumeration) #to get the answer of the picture
for i in range(100, 1000):

        val = str(i * 3)
        adder = str(i)
        if val[0]==val[1]==val[2] == adder[-1]:
                resp = f'{adder} + {adder} + {adder} = {val}'
                print(resp)
                break 


# exhaustive enumeration
# x = enter a number
# for i in range(1,1000)
# cube_root = i * i * i

test_value = 20 
step = 0
while step < 5:
        mutiple = step * step * step
        print(step, mutiple - test_value)
        if mutiple - test_value <= 0.5 and mutiple > test_value:
                print(f"Aproximate cube root of {test_value} is {step} because {step} cube is {step ** 3}")
                break
        
        step += 0.01

