# for i in range(1, 10):
	# print(i)
	# print("olatundefeyisayo")
	# input()

# x = 10 + 3 * 2 **2
# print(x)

# import math
# print(math.ceil (2.9))

# if is hot 
# it's a hot day
# drink plenty of water
# otherwise if it's cold
# it's a cold day 
# wear warm clothes
# otherwise
# it's a lovely day

# is_hot = False 
# is_cold = True
# if is_hot :
	# print("it's a hot day")
	# print("Dri
	# nk plenty of water")
# elif is_cold:
	# print("it's a cold day")
	# print("wear warm clothes")
# else:
	# print("it's a lovely day")
# print("\nEnjot your day")

# price of a house is $1m.
# if the buyer has good credit 
# they need to put down 10%
# otherwise
# they need to put down 20%
# print the down payment

price = 1000000
has_good_credit = True

# if has_good_credit:
	# down_payment = 0.1 * price
# else:
	# down_payment = 0.2 * price
# print(f"\nDown_payment: ${down_payment}")

# if applicant has high income and good credit
# elgible for loan

print("LOGICAL OPERATORS")
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
	print("\neligible for loan")

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
	print("\neligible for loan")

has_high_income = True
has_good_credit = False

if has_high_income or has_good_credit:
	print("\neligible for loan")

has_no_criminal_case = True
has_good_credit = True

if has_good_credit and not has_no_criminal_case:
	print("\neligible for loan")

has_criminal_record = False
has_good_credit = True

if has_good_credit and not has_no_criminal_case:
	print("\neligible for loan")

print("\n greater than".capitalize())
temperature = 30
if temperature > 30:
	print("it a hot day")
else:
	print("it is not a hot day")

print("\n less than".capitalize())
temperature = 30
if temperature < 30:
	print("it a hot day")
else:
	print("it is not a hot day")

print("\n equal to".capitalize())
temperature = 45
if temperature != 30:
	print("it a hot day")
else:
	print("it is not a hot day")
	

	