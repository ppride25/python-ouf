# Write your solution here

password=input("Password:")  

while True:
    rpassword=input("Repeat Password:")
    if password == rpassword:
        break
    else:
        print("They do not match!")

print("User account created!")