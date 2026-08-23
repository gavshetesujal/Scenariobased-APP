class Course:
    def __init__(self, course_name, duration, fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee

    def get_category(self):
        # Duration is assumed to be in months
        if self.duration <= 6:
            return "Short-Term"
        else:
            return "Long-Term"

    def display(self):
        print("Course Name:", self.course_name)
        print("Duration:", self.duration, "months")
        print("Fee: ₹", self.fee)
        print("Category:", self.get_category())
        print("------------------------")


class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self, course_name, duration, fee):
        course = Course(course_name, duration, fee)
        self.courses.append(course)

    def display_all_courses(self):
        print("Course Information")
        print("========================")

        for course in self.courses:
            course.display()


# Main Program
institute = Institute()

# Adding courses
institute.add_course("Python Programming", 3, 15000)
institute.add_course("Web Development", 6, 25000)
institute.add_course("Data Science", 12, 60000)
institute.add_course("Machine Learning", 9, 50000)

# Display all courses
institute.display_all_courses()
