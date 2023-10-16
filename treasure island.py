print("Welcome to treasure island!")
print("Your mission is to find the treasure.")
choice1 = input('you\'r at a crossroad, where do you want to go? Type "left" or "right".\n')
if choice1 == "left":
 choice2 = input('you\'ve come to a lake. Type "wait" to wait for the boat. Type "swim" to reach the island.\n')
 if choice2 == "wait":
    choice3 = input('A boat have taken you in a island. choose one door to get gold. Type "blue" or "yellow",or "green"').lower()
    if choice3 == "blue":
          print("Congrations!\nyou have got gold coins")
    else:
     print("This room is full of fire!\nGame Over.")
 else:
    print("This lake is full of trout!\nGame Over.")
else:
   print("Damn!There is a big hole.\nGame Over.")
