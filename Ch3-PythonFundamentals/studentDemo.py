# Build Student Class

class Student:

    def __init__(self, first, last, courses=None):
        self.first_name = first
        self.last_name = last
        if courses == None:
            self.courses = []
        else:
            self.courses = courses

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
        else:
            print(f"{self.first_name} is already \
                enrolled in the {course}.")

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"{course} not found")


    def __len__(self):
        return len(self.courses)

    # string representation for other devs
    def __repr__(self):
        return f"Student ('{self.first_name}','{self.last_name}','{self.courses}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()} \
               \nLast name: {self.last_name.capitalize()} \
                \nCourses: {', '.join(map(str.capitalize, self.courses))}"

courses1 = ['python', 'rails', 'javascript']
courses2 = ['java', 'rails', 'c']

tom = Student("tom", "Mac", courses1)
tom.remove_course('python')
tom.remove_course('python')

john = Student("john", "Wall", courses2)
john.add_course('rails')
john.add_course('javascript')

# print(tom.first_name, tom.last_name, tom.courses)
# print(john.first_name, john.last_name, john.courses)

print(tom)
# print(len(tom))
print(repr(tom))
# print(john)
# print(dir(tom))