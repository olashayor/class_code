

# fibonacci_cache = {}
# def fibonacci(n):
#     if  value in fibonacci_cache:
#         return fibonacci_cache(n)
    
#     if n == 0:
#         value = 0
#     elif n  == 1:
#         value = 1
#     elif n > 1:
#         value = fibonacci(n-1) + fibonacci(n-2)

# for n in range(0,50):
#     print(n, ":", fibonacci(n))
#     print(n, "-", fibonacci(n))

# fibonacci(n)


from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(n):
    
    if n == 0:
        return 0
    elif n  == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(0,50):
    print(n, ":", fibonacci(n))

fibonacci(n)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n  == 1:
#         return 1
#     elif n > 1:
#         return fibonacci(n-1) + fibonacci(n-2)

# for n in range(0,50):
#     print(n, ":", fibonacci(n))

# fibonacci(n)



# factorial asignent

# def factorial(n):
    
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    

# for n in range(1,10):
#     print(n, "factorial =", factorial(n))


# factorial(n)




