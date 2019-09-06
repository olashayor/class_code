# LIST

# students = ["azeez", "gozie", "abibat", "shayor", "samuel", "dijah", "kunle", "awele"]
# print(type(students))
# print(students)

# student2 = ("azeez")
# print(type(student2))
# print(student2)

# shopping_cart = ["apple", "coca cola", "soap", "chicken"]
# print(shopping_cart[-1])        #to get the last item on the shopping cart

# shopping_cart.append("pot")
# print(shopping_cart)
# print()

# ASSIGNMENT
# vowel = ["a", "e", "i", "o", "u"]
# consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
# vowel.count(vowel)
# consonant.count([])

# def count_element(list()):
#     elements = {}
#     for elem in list:
#         if elem in elements key()
#         elements[elem] += 1
#     else:
#         elements[]

# word = input("\nplease enter any word : \n".upper())
# x_b = reversed(word)
# vowel = ["a", "e", "i", "o", "u"]
# consonant = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
# emptylist_vowel = []
# emptylist_consonant = []
# emptylist_other_character = []
# count_vowel = 0
# count_consonants = 0
# count_other_character = 0

# for letters in word:
#     if letters in vowel:
#         count_vowel += 1
#         emptylist_vowel.append(letters)
        
#     elif letters in consonant:
#         count_consonants += 1
#         emptylist_consonant.append(letters)
#     else:
#         count_other_character +=1
#         emptylist_other_character.append(letters)

# unique_vowel = {letters:emptylist_vowel.count(letters) for letters in emptylist_vowel}
# unique_consonant = {letters:emptylist_consonant.count(letters) for letters in emptylist_consonant}
# unique_other_character = {letters:emptylist_other_character.count(letters) for letters in emptylist_other_character}

# print(f"\nThe reverse of the '{word}' is ", (list(x_b)))
# print("\nThere are", count_vowel, f"vowel in the word '{word}'")
# print(f"The vowels in the word '{word}' are", emptylist_vowel)
# print("The unique vowels are ", unique_vowel)
# print("\nThere are", count_consonants, f"consonants in the word '{word}'")
# print(f"The consonats in the word '{word}' are", emptylist_consonant)
# print("The unique consonant are ", unique_consonant)
# print("\nThere are", count_other_character, f"other character in the word '{word}'")
# print(f"The other characters in the word '{word}' are", emptylist_other_character)
# print("The unique characters are ", unique_other_character)

# GREAT!!! YOU ARE CORRECT

# TEACHERS ANSWER
user_text = input("please enter text to work on : ")

# reverse using silincing
reversed_user_text = user_text[::-1]
print(reversed_user_text)

consonant = ""
vowels = ""

vowel_count = 0 
consonant_count = 0 

vowels_in_english = "aeiou"
for letter in user_text:

    if letter in vowels_in_english:
        vowel_count += 1
        if letter not in vowels:
            vowels += letter

    elif letter not in vowels_in_english and letter.isalpha():
        consonant_count += 1
        if letter not in consonant:
            consonant += letter
         
print(f"Vowels = {vowel_count}, cons = {consonant_count}, \n O-chars = {len(user_text) - consonant_count - vowel_count}, Total = {len(user_text)},  \n\n unique consonant - {consonant} \n uniqque vowels = {vowels} ")


# LIST COMPREHESION
# my_number_list = [1,2,3,4,5,6,7,8]
# my_number_list2 = []

# for i in range(1,9):
#     my_number_list2.append(i)
#     name = "ada"
# my_number_list_with_list_comp = [i for i in name]
# print(my_number_list_with_list_comp)

number = [x for x in range(20)]
print("number is ", number)
numbersquare = [x**2 for x in number]
print("number square is ", numbersquare)
x_bar = sum(number)/len(number)
print("x bar is ", x_bar)

x_xbar = [x - x_bar for x in number]
print("x - x bar is ", x_xbar)

negative_num = x_xbar[0:10]                 #[star:stop:step]
print("1st", negative_num)
positive_num = x_xbar[11:20]
print("2nd", positive_num)
positive_num = x_xbar[10:-1:2]                 #2step motion
print("3rd", positive_num)

positive_num = x_xbar[::-1]      #1step backward motion
print("4th", positive_num)

products = ["dried beans", "canned corn", "jewelry", "quality funiture", "automobile parts"]

reversed_products = products[::-1]
print(reversed_products)

# to print id(last 3 digit) and name alone
number = [("ade", 1220031203), ("jolade", 1220031205), ("shade", 1220031208), ("azeez", 1220031209)]
print("Name".center(10), "ID".center(5))
for person in number:

    print(f"{person[0]}".center(10), f"{str(person[1]) [-3:]}".center(5))

# TO LIST THE ALPHABETHS IN THE NAME
for person in number:
    print(person[0])  
    for letter in person[0]:
        print(f"{letter}")



# combs = [ ]
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x,y))
# print(combs)
               
# combs = [(x,y)for x in [1,2,3]for y in [3,1,4] if x != y]
# print(combs)

# squares = []
# for x in range(10): 
#     squares.append(x**2)
# print(squares)



