print("Please type in integer numbers. Type in 0 to finish.")
numbers = 0
sum = 0
positives = 0
 
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    numbers += 1
    sum += number
    if number>0:
        positives += 1
 
print("Numbers typed in", numbers)
print("The sum of the numbers is", sum)
print("The mean of the numbers is", sum/numbers)
print("Positive numbers", positives)
print("Negative numbers", numbers-positives)