# Write your solution here
sum = int(input("Value of gift:"))

if sum < 5000:
    print("No tax!")
elif sum >= 5000 and sum < 25000:
    tax = 100 + (sum - 5000) * 0.08
    print(f"Amount of tax: {tax} euros")
elif sum >= 25000 and sum < 55000:
    tax = 1700 + (sum - 25000) * 0.10
    print(f"Amount of tax: {tax} euros")
elif sum >= 55000 and sum < 200000:
    tax = 4700 + (sum - 55000) * 0.12
    print(f"Amount of tax: {tax} euros")
elif sum >= 200000 and sum < 1000000:
    tax = 22100 + (sum - 200000) * 0.15
    print(f"Amount of tax: {tax} euros")
else:
    tax = 142100 + (sum - 1000000) * 0.17
    print(f"Amount of tax: {tax} euros")



#Model Solution

value = int(input("Value of gift: "))
 
if value < 5000:
    tax = 0
elif value <= 25000:
    tax = 100 + (value - 5000) * 0.08
elif value <= 55000:
    tax = 1700 + (value - 25000) * 0.10
elif value <= 200000:
    tax = 4700 + (value - 55000) * 0.12
elif value <= 1000000:
    tax = 22100 + (value - 200000) * 0.15
else:
    tax = 142100 + (value - 1000000) * 0.17
 
if tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")
 