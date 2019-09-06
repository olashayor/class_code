# x = 0
# y = 5

# if x < y:
#     print('yes')
#     print("y is", bool(y), "x is", bool(x), "and the if statement got", x < y)

# test = "shayo"
# name = "feyisayo"
# letter = "a"

# if test in name:
#     print('yes', name, "contains ", test)
# elif letter in name:
#     print(name, 'does not contain', test, ". But contains", letter)
# else:
#     print(name, 'does not contain', test, " and does not contain", letter)


# print("\nassignment".upper)
# name = input("please enter your name:")
# if "a" in name:
#     print("name contains a vowel sound")
# elif "e" in name:
#     print("name contains a vowel sound")
# elif "i" in name:
#     print("name contains a vowel sound")
# elif "o" in name:
#     print("name contains a vowel sound")
# elif "u" in name:
#     print("name contains a vowel sound")
# else:
#     print(name, "does not contain a vowel sound")

# num1 = input("please type the first number : ")     #type the first number
# num2 = input("please type the second number : ")    #type the second number
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1 < num2:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("the two numbers are equal".upper())


# question = input("do you have headache? yes = y, no = n : ")
# if question == "y":
#     fever = input("do you have fever? "):
#         if fever == "y":
#     vomiting = input ("are you vomiting? ")
# elif question == "n":
#     print("you are okay, no problem ")
# elif fever == "n":
#     print("you are only stressed out ")
# elif vomiting == "y":
#     print("you have thyphoid ")
# elif vomiting == "n":
#     print("you have malaria ")
# else:
#     print("you are okay no problem ")                                                                                                                                                                                                                                                                                                                 


print("solution".upper)
headache_response = input("Do you have a headache .? reponse y/n : ")       #check for head_ache
if headache_response == "y":

    fevever_reponse = input("Do you have a fever .? reponse y/n : ")        #check for fever

    if fevever_reponse == "y":

        vomit_reponse = input("Have you vomitted .? reponse y/n : ")        #check for vomit

        if vomit_reponse == "y":
            print("You have typhoid, please see a doctor")
   
        elif vomit_reponse == "n" :
            print("You have malaria, please see a doctor")

    elif fevever_reponse == "n":
        print("You are probably streessed out, try to rest")

elif headache_response == "n":
    print("You are probably okay or maybe see a medical practitioner")

# if <expr>: <statement_1>; <statement_2>;....; <statement_n>
# x = 20
# if x == 20 : print(x), print("next statement"), ("happy syntax")
# probably unreadable syntax too many single line statements
# if x == 20 : break #accceptable

# TENARY OPERATOR

"""<expr1> if <conditional_expr> else <expr2>"""

# user_name = input("please enter your name in caps")
# name = user_name if user_name.isupper() else "input was not upper case"

# print(name)

score = int(input("please enter your student score"))

status = "Qualified" if score >= 60 else "Not qualified"
print(status)

student_is_qualified = True if score >= 60 else False

if student_is_qualified :
    print("\nSend mail to student\n")
    print("content: You have have qualified for admission please visit our page to continue your registration")