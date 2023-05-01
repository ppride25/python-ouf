from math import sqrt

while True:
    num=int(input("Please type in a number: "))
    if num == 0:
        break
    if num >0:
        print(sqrt(num))
    else:
        print("Invalid number")
    
print("Exiting...")
