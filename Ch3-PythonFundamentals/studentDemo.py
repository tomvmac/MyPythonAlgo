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

    def find_in_file(self, filename):
        with open(filename) as f:
            for line in f:
                first_name, last_name, course_details = Student.prep_record(line.strip())
                student_read_in = Student(first_name, last_name, course_details)
                if self == student_read_in:
                    return True
            return False

    def add_to_file(self, filename):
        if self.find_in_file(filename):
            return "Record already exists"
        else:
            record_to_add = Student.prep_to_write(self.first_name, self.last_name, self.courses)
            with open(filename, "a+") as to_write:
                to_write.write(record_to_add + "\n")
            return "Record added"

    @staticmethod
    def prep_record(line):
        line = line.split(":")
        first_name, last_name = line[0].split(",")
        course_details = line[1].rstrip().split(",")
        return first_name, last_name, course_details

    @staticmethod
    def prep_to_write(first_name, last_name, courses):
        full_name = first_name + ',' + last_name
        courses = ",".join(courses)
        return full_name + ":" + courses

    def __eq__(self, other):
        return self.first_name == other.first_name \
        and self.last_name == other.last_name

    def __len__(self):
        return len(self.courses)

    # string representation for other devs
    def __repr__(self):
        return f"Student ('{self.first_name}','{self.last_name}','{self.courses}')"

    def __str__(self):
        return f"First name: {self.first_name.capitalize()} \
               \nLast name: {self.last_name.capitalize()} \
                \nCourses: {', '.join(map(str.capitalize, self.courses))}"


#inheritance
class StudentAthlete(Student):
    def __init__(self, first, last, courses=None, sport=None):
        super().__init__(first, last, courses)
        self.sport = sport

# files
file_name = "data.txt"

courses1 = ['python', 'rails', 'javascript']
courses2 = ['java', 'rails', 'c']

tom = Student("tom", "mac", courses1)
# tom.remove_course('python')
# tom.remove_course('python')

# john = Student("john", "Wall", courses2)
# john.add_course('rails')
# john.add_course('javascript')

# print(tom.first_name, tom.last_name, tom.courses)
# print(john.first_name, john.last_name, john.courses)

# print(tom)
# print(len(tom))
# print(repr(tom))
# print(john)
# print(dir(tom))

# find and add student
print(tom.find_in_file(file_name))
print(tom.add_to_file(file_name))

# joe = Student("joe", "schmo", ["python", "ruby", "javascript"])
# print(joe.find_in_file(file_name))
# print(joe.add_to_file(file_name))

jane = StudentAthlete("jane", "doe", courses2, "basketball")
print(jane)
print(jane.sport)
print(isinstance(jane, StudentAthlete))
print(isinstance(jane, Student))
