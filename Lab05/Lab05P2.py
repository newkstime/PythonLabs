#Write a program for course registration
print("Welcome to Course Registration."
      "\nTo add a new course, input A."
      "\nTo drop a course, input D."
      "\nTo exit the program, input E.")
selection = input("Please make a selection:")
courseList = []
while selection.lower() == "a" or selection.lower() == "d":
    #If the user enters A, add the course
    if selection.lower() == "a":
        addCourse =  input("Please enter the course to be added:")
        if addCourse.upper() not in courseList:
            courseList.append(addCourse.upper())
            print("Course added.")
        else:
            print("You are already registered for that course.")
        courseList.sort()
        print(courseList)
        selection = input("Please make a selection:")
    #If the user enters D, drop the course
    elif selection.lower() == "d":
        removeCourse = input("Please enter a course to drop:")
        if removeCourse.upper() in courseList:
            courseList.remove(removeCourse.upper())
            print("Course dropped.")
        else:
            print("You are not registered for that course.")
        courseList.sort()
        print(courseList)
        selection = input("Please make a selection:")
#If the user enters E, exit the program
if selection.lower() == "e":
    print("Goodbye.")
else:
    print("Invalid input.")
