courses = []

with open("course.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        courses.append(f"{language} -{category}")

for course in sorted(courses, reverse=True):
    print(course)
