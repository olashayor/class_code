# def do_something():
#     """this fuction does nothing"""

#     if True:
#         print("hello  function")

# do_something()  # function call

# def greet(person):
#     person = capitalize(person)
#     print(f"hello {person}.")

# def capitalize(word):
#     return word.capitalize()

# user = "Bola"
# user1 = "Shayor"
# user2 = "Attah"
# user3 = "Dayo"
# greet(user)
# greet(user1)
# greet(user2)
# greet(user3)

# users = ["attah", "bola", "shayor"]

# for user in users:
#     greet(user)

# def dict_sum(_dict):
#     sum = 0
#     for key in _dict:
#         print(key)
#         sum += _dict[key]

#     print(sum)

# students_per_class = {"ss1":15, "ss2":20, "ss3":34}
# dict_sum(students_per_class)


# def calculate_fraction():

#     num1 = int(input("\nenter the numerator of the first fraction : "))
#     denum1 = int(input("\nenter the denumerator of the first fraction : "))
#     num2 = int(input("\nenter the numerator of the second fraction : "))
#     denum2 = int(input("\nenter the numerator of the second fraction : "))
#     denumerator = denum1 * denum2
#     numerator = (denum2 * num1) + (denum1 * num2)

#     print(f"\nthe addition of the faction is {numerator}/{denumerator}")

# calculate_fraction()


# ASSIGNMENT
def calculate_fraction():

    num1 = int(input("\nenter the numerator of the first fraction : "))
    denum1 = int(input("\nenter the denumerator of the first fraction : "))
    num2 = int(input("\nenter the numerator of the second fraction : "))
    denum2 = int(input("\nenter the numerator of the second fraction : "))
    denumerator = denum1 * denum2
    numerator = (denum2 * num1) + (denum1 * num2)

    print(f"\nthe addition of the faction is {numerator}/{denumerator}")
    return (f'{numerator}/{denumerator}')


def lowest_factor(val):
    
    val = val.split('/')
    numerator = int(val[0])
    denumerator = int(val[1])
    # if denumerator % numerator == 0:
    #     print(f"The lowest multiple is {int(numerator / numerator)}/{int(denumerator / numerator)}")
    print(f"\nthe addition of the faction is {numerator}/{denumerator}")
        
    x = 0
        
    while x < 50:

        
        for i in reversed(range(2,11)):

            if (numerator % i == 0) and (denumerator % i == 0):

                numerator = int(numerator / i)
                denumerator = int(denumerator / i)
                print(f"\nTo divide by {i} is {numerator}/{denumerator}")
                # print("To divide again")
            
            else:
                pass
        x += 1

    print(f"\nFinal answer is {int(numerator)}/{int(denumerator)}")
    
    # else:
    #     print("The fraction is not divisible without reminder")
    
lowest_factor(calculate_fraction())



# ANOTHER STYLE
#calculate_fraction()
# def simplefy_fraction(numerator,denumerator):
#     for divisor in reversed(range(2,11)):
#         print("Testing with ", divisor)
#         while numerator % divisor == 0 and denumerator % divisor == 0 :
#             numerator = numerator / divisor
#             denumerator = denumerator / divisor

#             print(numerator,"/",denumerator)

#     print(f"The final aswer {numerator}/{denumerator}")

# simplefy_fraction(numerator,denumerator)      








