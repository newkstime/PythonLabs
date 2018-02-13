counter = 0
height = float(input("Enter the height from which the ball is dropped in feet:"))
bounciness = float(input("Enter the bounciness index of the ball:"))
timesBounced = int(input("Enter the number of times the ball is allowed to bounce:"))
while counter < timesBounced:
    height = height * bounciness
    print("On bounce #", counter, "the ball bounced:", height, "feet.")
    counter += 1
