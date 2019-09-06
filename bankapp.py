
import ast

class BankApplication():
    def __init__(self):
        self.name = name
        self.number = 309684
        self.balance = 0

    def __read_all(self):
        with open('new.txt', 'r') as file:
            data = file.read()

            file.close()
            return {} if len(data)<1 else ast.literal_eval(data)

    def depositbank(self):
        data = self.__read_all()
        trial = 0
    
        while trial < 3:
            verify = input("please enter your password : ")
            if verify in data:
                depo = int(input("enter the amount you want to deposit : "))
                self.balance += depo
                print("You new balance is : ", self.balance)
                break

            else:
                print("Incorrect password")
            
            return self.balance
        



    def withdrw(self):
        data = self.__read_all()
        trial = 0

        while trial > 3: 
            verify = input("please enter your password : ")
            if verify in data:
                withdw = int(input("Enter the amount you want to withdraw : "))
                if self.balance > withdw:
                    self.balance -= withdw
                    print("You new balance is : ", self.balance)
                    break
                
                else: 
                    print("Insufficient balance!! ")
                
            else:
                print("Incorrect pasword!! ")

            trial += 1

            return self.balance
        


    def transfer(self):
        data = self.__read_all()

        verify = input("please enter your password : ")
        if verify in data:
            input("Enter the the acount name you want to transter to : ")
            amount = int(input("Enter the account number to transfer to : "))
            if amount < self.balance:
                self.balance -= amount
                print("Your new balance is ", self.balance)
            
            else:
                print("Insufficient balance")
        
        else:
            print("Incorrect Password")
        
        return self.balance


class User():
    def __init__(self, name = 'user'):
        self.name = name
        self.detail = Storage(self).read()

    def create(self):
        name = input("please enter your name : ")
        age = int(input("please enter your age"))
        gender = (input("please enter your gender"))
        password = (input("set a for your account"))
        detail_to_save = Account(name, age, gender, password)
        storage_object = Storage(self)
        storage_object.save(detail_to_save)


    def view_account(self):
        detail_from_file = Storage(self).read()
        print(f"Hello {user} below is ur account detail:\n\t ")
        for detail in detail_from_file:
            print(f"\t {detail[0]} --> {detail[1]}")

        


class Storage():
    def __init__(self, user):
        self.name = user
        self.balance = 0

    def save(self, detail_to_save):
        data = self.__read_all()
        reg_user = dict(data.keys())
        detail = detail_to_save.name, detail_to_save.age, detail_to_save.gender, detail_to_save.password, detail_to_save.number, detail_to_save.balance 

        if self.name in reg_user:
            data[self.name].update(detail)

        else:
            data[self.name] = {}
            data[self.name].update(detail)

        with open('new.txt', 'w') as file:
            file.writelines(str(data))

            file.close()

    
    def deposit(self):
        pass


    def withdraw(self):
        pass




    def read(self):
        with open('new.txt', 'r') as file:
            data = file.read()

            file.close()
            try:
                return {} if len(data)<1 else ast.literal_eval(data)[self.user.name]
            except:
                return "NO DETAIL AVAILABLE"


 

    def close_account(self):
        data = self.__read_all()
        
        verify = input("Enter your password : ")
        if verify in data:
            data.clear()
            print(data)

        else:
            print("Incorrect password!")
    
class Account():

    def __init__(self, name = 'none', age = 0, gender = 'null', password = 0, number = 3096684):
        self.intial_bal = 0
        self.name = name
        self.age = age
        self.gender = gender
        self.password = password
        self.number = 3096684


zenith = BankApplication()
user.create()
# BankApplication(name = 'john adio', age = 22, gender = 'male', password = 'bill')
user = User(name = 'John Adio')
user.view_account()

question = input("What do you want to do : ")
while question != "close account":
    if question == "creat account":
        User.create()
    elif question == "deposit":
        BankApplication.depositbank()
    elif question == "transfer":
        BankApplication.transfer()
    elif question == "login":
        User.login
    elif question == "withdraw":
        BankApplication.withdrw()






    # def check_balance(self):
    #     self.balance = balance

    #     verify = input("please enter your password : ")
    #     if verify in reg_user:
    #         print("Your present balance is  #",balance)
