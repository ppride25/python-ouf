atemps = 0
while True:
    pin = int(input("PIN: "))
    atemps=atemps + 1
    if pin == 4321:
        break
    else:
        print("Wrong")
if atemps == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {atemps} attempts")