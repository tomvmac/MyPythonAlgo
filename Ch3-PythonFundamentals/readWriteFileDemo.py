# Read & Write File Demo

# Write functions for the following:
# Function to convert string to parameters for __init__
# Function to  convert Student object to string for write to file
# special function - equality test

file_name = "data.txt"
# first_name = "tom"
# last_name = "mac"
# courses = ['python', 'ruby', 'javascript']

# open a file
# file_name = "data.txt"
# f = open(file_name)
# # f_contents = f.readline()
# #f_contents = f.read()
# # print(f_contents)
#
# for line in f:
#     print(line.strip())
#
# f.close()


def prep_record(line):
    line = line.split(":")
    first_name, last_name = line[0].split(",")
    course_details = line[1].rstrip().split(",")
    return first_name, last_name, course_details


# prep_to_write takes in info and transforms to record format to add - "john, schomoe:python, ruby, javascript"
def prep_to_write(first_name, last_name, courses):
    full_name = first_name + ',' + last_name
    courses = ",".join(courses)
    return full_name + ":" + courses

# opening files with context manager - does all the close and clean up
with open(file_name) as f:
    for line in f:
        print(line.strip())
        first_name, last_name, course_details = prep_record(line)
        print(first_name, last_name, course_details)

to_write = prep_to_write("james", "harden", course_details)
print(to_write)
record_to_add = "john,schomoe:python, ruby, javascript"

with open(file_name, "a+") as to_write:
    to_write.write(record_to_add + "\n")