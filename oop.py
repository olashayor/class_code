# class Person:  #class declaration
#     mouth = 1
#     hand = 2
#     legs = 2

#     def __init__(self,eye_colour = "black", skin_colour = "fair"): #initializer for instance for variables
#         self.eye_colour = eye_colour
#         self.skin_colour = skin_colour

#     def walk(self):
#         print("walking on foot")

# class Politician(Person): #class declaration
#     run_for_office = True

#     def walk(self):
#         print("Too fresh, Flying private .")

# saraki = Politician("grey", "dark")
# ade = Person(eye_colour = "brown", skin_colour = "Pale")    # an object(instance of a class)
# bolu = Person("red", "black")   #an object (instance of a class)
# bola = Person("blue", "extra black")    #an object (intance of a class)




class Car:
    wheel = 4
    side_mirror = 2
    brake = 1
    head_light = 2

    def __init__(self, colour = "black", seat = "leather", wiper = 2):
        self.car_colour = colour
        self.seat_type = seat
        self.car_wiper = wiper 
    
    def start(self):
        print("The car is starting")
    
    def toggle_light(self):
        print("The light is on ")

matrix = Car()
print(matrix)

