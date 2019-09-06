name = "Oluwafeyisayisayomi"

print(name)

name = input( "please enter your name : ")

print('your name is', name)

for i in range (1,200):
    print(i) 

c = input("please entre Temperature in celsius : ")
farenheit = (int(c) * 1.8) + 32
print('Temperature in farenheit', farenheit, )

first_item = input("please enter first item name : ")
item1_price = int(input("please enter first item price : "))
item1_qty = int(input("please enter first item qty : "))

second_item = input("please enter second item name : ")
item2_price = int(input("please enter second item price : "))
item2_qty = int(input("please enter second item qty : "))

third_item = input("please enter third item name : ")
item3_price = int(input("please enter third item price : "))
item3_qty = int(input("please enter third item qty : "))

fourth_item = input("please enter fourth item name : ")
item4_price = int(input("please enter fourth item price : "))
item4_qty = int(input("please enter fourth item qty : "))

print(first_item, item1_price, item1_qty, item1_price * item1_qty)
print(second_item, item2_price, item2_qty, item2_price * item2_qty)
print(third_item, item3_price, item3_qty, item3_price * item3_qty)
print(fourth_item, item4_price, item4_qty, item4_price * item4_qty)

total_stock = (item1_price * item1_qty) + (item2_price * item2_qty) +(item3_price * item3_qty) + (item4_price * item4_qty)

print(total_stock)

first_item = "bags"
item1_price = 25
item1_qty = 10

second_item = "shoe"
item2_price = 20
item2_qty = 13

third_item = "shirt"
item3_price = 10
item3_qty = 20

fourth_item = "skirt"
item4_price = 9
item4_qty = 10

print("Name".center(13), "Price".center(13), "Qty".center(13), "Total".center(13), "\n")
print(first_item.center(13), str(item1_price).center(13), str(item1_qty).center(13), str(item1_price * item1_qty).center(13))
print(second_item.center(13), str(item2_price).center(13), str(item2_qty).center(13), str(item2_price * item2_qty).center(13))
print(third_item.center(13), str(item3_price).center(13), str(item3_qty).center(13), str(item3_price * item3_qty).center(13))
print(fourth_item.center(14), str(item4_price).center(12), str(item4_qty).center(13), str(item4_price * item4_qty).center(13))

total_stock = (item1_price * item1_qty) + (item2_price * item2_qty) +(item3_price * item3_qty) + (item4_price * item4_qty)

print("TOTAL STOCK IS ", total_stock)
