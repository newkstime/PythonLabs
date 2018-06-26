class Course:
    def __init__(self, course_code, quota):
        self.course_code = course_code
        self.quota = quota
        self.enrollment = 0

    def add_student(self):
        if self.enrollment < self.quota:
            self.enrollment += 1
            print("One student added.")
        else:
            print("Course is already full.")

    def drop_student(self):
        if self.enrollment > 0:
            self.enrollment -= 1
            print("One student dropped.")
        else:
            print("Course is empty")
