# lambda functions = functions written in 1 line using lambda keyword
#                    accepts any number of arguments, but only has one expression.
#                    (think of it as a shortcut)
#                    (useful if needed for  a short period of time, throw away)
# lambda parameters:expression


#def double(x):
#   return x * 2

#print(double(5))


multiply = lambda x, y: x * y
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False
test = lambda test: test + test




print(double(5))
print(multiply(4,5))
print(full_name("allen", "harper"))
print(age_check(19))

def check(letter):
    return letter > 0



print(check(5))