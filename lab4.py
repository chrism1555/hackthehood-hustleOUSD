checking = "yes"

while checking == "yes":
    print("What is your age: ")
    user_input = input ()
    if int(user_input) >= 18:
        print("Yes you can vote")
    else:
        print ("You can't vote")
    print("Would you like to check another age?")
    user_input2 = input ( )
    checking = user_input2

list1 = [3, -1, 0, 6, -4]

for x in list1:
    if x > 0:
         print("value is positive")
    elif x < 0:
         print("Value is negative")
    else:
         print("Number is zero")

inventory = ["egg", "gold", "axe", "sword", "flint", "coal", "water bucket"]
for i in inventory:
    if i == "flint":
        print("ore")
    elif i == "axe":
        print("equipment")