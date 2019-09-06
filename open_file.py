import random
file = open("twist.txt" , 'r')
print(file)

print("\nYou are welcome to my word game! \nI'm thinking of a word between two and four letter words \nYou have 5 guess to guess all the letters in the word \nlets get started!!! ".upper())
for text in file:
    do = (text.split())
    

word = random.choice(do)

print(word)
trial = 0
word_copy = list(word).copy()
lenght = len(word)
guess_word = list(("-" * lenght))
limit = 5
hint = word[0][-1]

print(f"\nthe word is a {lenght} letter word".upper())

while trial < 5:
    print(guess_word)
    guess_leter = input("\nguess a letter from the word : ".upper())

    for letter in guess_leter:
        trial += 1
        if letter in word:
            print("YES!!")
            print(letter)


            index_spaces = word_copy.index(letter)
            word_copy[index_spaces] = "-"
            guess_word[index_spaces] = letter 
            
            if guess_word == list(word):
                print(f"BRAVO!!! \nYou are correct the word is {word}")
                break

              
        else: 
            print("NO! \nTry again")
                
            if trial == 3:
                hint = word[0],word[-1]
                print(f"\nThe first and the last letter of the word is {hint} respectively\n")


        # if guess_word == list(word):
        #     print(f"BRAVO!!! \nYou are correct the word is {word}")
        #     break



else:
    print(f"VERY BAD you have exceeded you limit the word is {word}")
    






                        


#  DICE GAME
import random
print("\nlets play dice game".upper())
print("\nyou are going to are going to throw the dice first and then me, \nany one with the highest number wins".upper())
turn = 0
player1 = 0
player2 = 0
input("PRESS ENTER TO START : ")
while turn < 5:
    turn += 1
    print(f"\nFor turn {turn}\n".upper())
    player1_dice1 = random.randint(1,6)
    player1_dice2 = random.randint(1,6)
    player1 = player1 + player1_dice1 + player1_dice2
    print(f"player one dice {player1_dice1}, and {player1_dice2}")

    player2_dice1 = random.randint(1,6)
    player2_dice2 = random.randint(1,6)
    player2 = player2 + player2_dice1 + player2_dice2
    print(f"player two dice {player2_dice1}, and {player2_dice2}")

    print(f"\nTotal score for player one is {player1}")
    print(f"\nTotal score for player two is {player2}\n")
    
    input("Press enter to continue : ")
    

if player1 > player2:
    print("\nplayer one won".upper())

elif player1 < player2:
    print("\nplayer two won".upper())

else:
    print("\nno winner".upper())





