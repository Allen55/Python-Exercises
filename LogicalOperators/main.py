temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good outside")
    print("Go outside")
elif temp < 0 or temp > 30:
    print("Stay inside")