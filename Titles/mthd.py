class student:

    created_instances = 0

    def __init__(self, name, age, course, school):
        self.name = name
        self.age = age
        self.course = course
        self.school = school
        student.created_instances += 1


    def course_(self, course1):
        self.course = course1

    def display_stud(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("School:", self.school)

    @classmethod
    def update_school(cls, new_school):
        cls.school = new_school

    @staticmethod
    def total_students(cls):
        print("Total number of students:", cls.created_instances)

    @staticmethod
    def is_adult(age):
        return age >= 18

    @staticmethod
    def is_course(course):
        return course.lower() in ["computer science", "data science", "engineering"]



def main():
    student1 = student("Alice", 20, "Computer Science", "XYZ University")
    student2 = student("Bob", 17, "Data Science", "ABC College")

    student1.display_stud()
    print()
    student2.display_stud()
    print()

    # Update course for student1
    student1.course_("Artificial Intelligence")
    print("Updated Course for Student 1:")
    student1.display_stud()
    print()

    # Update school for all students
    student.update_school("New School Name")
    print("Updated School for Student 1:")
    student1.display_stud()
    print("Updated School for Student 2:")
    student2.display_stud()
    print()

    # Display total number of students
    student.total_students(student)
    print()


main()