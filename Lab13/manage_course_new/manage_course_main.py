from course import Course

course_code = input("Please enter the course code:")
quota = ""
while isinstance(quota, int) == False:
    try:
        quota = int(input("Please enter the maximum number of students allowed in the course:"))
        while quota <= 0:
            print("Maximum student must be at least 1.")
            quota = int(input("Please enter the maximum number of students allowed in the course:"))
    except ValueError:
        print("Invalid entry")

course1 = Course(course_code, quota)

user_input = ""
while user_input != "0":
    user_input = input("""Enter 1 to add a student to the course.
Enter 2 to drop a student from the course.
Enter 3 to view course info.
Enter 4 to change the course quota
Enter 0 to exit.\n""")
    if user_input == "1":
        course1.add_student()
        print("Enrollment:", course1.get_enrollment(), "\n")
    elif user_input == "2":
        course1.drop_student()
        print("Enrollment:", course1.get_enrollment(), "\n")
    elif user_input == "3":
        print("Course code: " + course1.get_course_code() + "\nCourse Quota: " + str(course1.get_quota()) + "\nEnrollment: " + str(course1.get_enrollment()), "\n")
    elif user_input == "4":
        quota = ""
        while isinstance(quota, int) == False:
            try:
                quota = int(input("Please enter the maximum number of students allowed in the course:"))
                while quota <= 0:
                    print("Maximum student must be at least 1.")
                    quota = int(input("Please enter the maximum number of students allowed in the course:"))
            except ValueError:
                print("Invalid entry")
        course1.set_quota(quota)
        print("New Quota set.")
    elif user_input != "0":
        print("Invalid entry.\n")

