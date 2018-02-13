aqua_visits = int(input("Input the number of visitors for only the Aquarium:"))
threeD_visits = int(input("Input the number of visitors for only the 3D Show:"))
combo_visits = int(input("Input the number of visitors seeing both shows:"))
aqua_visits_cost = aqua_visits * 14.0
threeD_visits_cost = threeD_visits * 8.0
combo_visits_cost = combo_visits * 16.5
print("The total cost of admission is: $", format(aqua_visits_cost + threeD_visits_cost + combo_visits_cost, '.2f'))
