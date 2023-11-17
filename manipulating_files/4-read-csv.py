with open("course.csv", "r", encoding="utf-8") as file:
    for line in file:
        # row = line.rstrip().split(",")
        # print(row)
        language, category = line.rstrip().split(",")
        print(f"{language} -{category}")
