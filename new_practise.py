def emoji_covert(message):
    words = message.split(" ")
    emoji = {":)": "HAPPY!", ":(": "SAD"}
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output

message = input("how do u feel? ")
print(emoji_covert(message))

class Person:
    def __init__(self):
        self.name = name 

    def talk(self):
        print("I can talk")