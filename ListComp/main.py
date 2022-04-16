# list comprehension = a way to create a new list with less syntanx
#                      can mimic certain lambda functions, easier to read
#                      list = [expression for item in iterable]
#                      list = [expression for item in iterable if conditional]
#                      list = [expression if/else for item in iterable]

squares = []
for i in range(1, 11):
    squares.append(i*i)
print(squares)

squares2 = [i * i for i in range(1, 11)]
print(squares2)


nums = [1,2,3,4,5,6,]

list_comp = [i * 2 for i in nums]
print(list_comp)


list2 = lambda x : x +1
print(list2(2))







lamb1 = lambda x: abs(x)


list_comp2 = [i * 10 for i in range(10)]

print(lamb1(-31))
print(list_comp2)

squares3 = [i * i for i in range(0, 3)]
print(squares3)














