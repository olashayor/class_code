# for i in range(100,999):
    
#     val = str(i * 3)
#     adder = str(i)
#     if val[0==val[2 == adder[-1]:
#         resp = f'{adder} + {adder} + {adder}  = {val}'
#         print(resp)
#         break



test_value = int(input("enter a value"))
step = 0

while step < 5:

    multiple = step * step * step
    # print(step, multiple)

    # print(step, multiple - test_value)

    if multiple - test_value <= 0.5 and multiple >= test_value:

        print(f"""Approximate cube root of {test_value} is {step} 
                because  {step} cube is {step ** 3}""")

        break

    step += 1