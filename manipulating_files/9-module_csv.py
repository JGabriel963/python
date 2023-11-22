import csv

courses = []
with open("course.csv", "r", encoding="utf-8") as file:
    #    reader = csv.reader(file)
    #    for name, category in reader:
    #        languagens.append({"name": name, "category":category})
    reader = csv.DictReader(file)
    for row in reader:
        courses.append({"language": row["language"], "category": row["category"]})

for course in sorted(courses, key=lambda course: course["category"]):
    print(f"{course['language']} - {course['category']}")
