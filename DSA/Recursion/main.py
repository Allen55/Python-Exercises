

def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)

"""
5 + (5 - 1 = 4)
        5 + (4 - 1 = 3)
                5 + (3 - 1 = 2)
                        5 + (2 - 1 = 1)


"""

def fib(n):
    if n == 0 or n == 1:
        return n

    return fib(n - 1) + fib(n - 2)


print(find_sum(5))
print(fib(6))