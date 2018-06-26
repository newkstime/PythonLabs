from drone import Drone

drone1 = Drone()
keep_going = True
while keep_going == True:
    user_input = input("Enter 1 for accelerate, 2 for decelerate, 3 for ascend, 4 for desend, 0 to exit:")
    if user_input == "1":
        drone1.accelerate()
    elif user_input == "2":
        drone1.decelerate()
    elif user_input == "3":
        drone1.ascend()
    elif user_input == "4":
        drone1.descend()
    elif user_input == "0":
        keep_going = False
    else:
        print("Unrecognized command.")
    print (drone1)
