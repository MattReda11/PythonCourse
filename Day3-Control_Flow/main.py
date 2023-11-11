print("Welcome to Treasure Island.\nYour mission is to find the treasure!")
side_decision = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")


if(side_decision == "right"):
    print("You fell in a hole. Game Over.")
elif(side_decision == "left"):
    lake_decision = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat, or 'swim' to swim to the island.\n")

    if(lake_decision == "swim"):
        print("You were attacked by a hungry shark. Game Over.")
    elif(lake_decision == "wait"):
        door_decision = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n")

        if(door_decision == "red"):
            print("It's a room full of fire! Game Over.")
        elif(door_decision == "yellow"):
            print("You found the treasure! You Win.")
        elif(door_decision == "blue"):
            print("You entered a room full of savage beasts! Game Over.")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Invalid choice. Game Over.")