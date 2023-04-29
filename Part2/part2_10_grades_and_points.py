# Write your solution here

grade=int(input("How many points [0-100]:"))

if grade < 0:
    print("impossible!")
elif grade >= 0 and grade <= 49:
    print("Grade: fail")

elif grade >=50 and grade <= 59:
    print ("Grade: 1")

elif grade >=60 and grade <= 69:
    print ("Grade: 2")

elif grade >=70 and grade <= 79:
    print ("Grade: 3")

elif grade >=80 and grade <= 89:
    print ("Grade: 4")

elif grade >=90 and grade <= 100:
    print ("Grade: 5")

else:
    print("impossible!")


#Model Result
# points = int(input("How many points [0-100]: "))
 
# if points < 0 or points > 100:
#     grade = "impossible!"
# elif points < 50:
#     grade = "fail"
# elif points < 60:
#     grade = "1"
# elif points < 70:
#     grade = "2"
# elif points < 80:
#     grade = "3"
# elif points < 90:
#     grade = "4"
# else:
#     grade = "5"
 
# print(f"Grade: {grade}")