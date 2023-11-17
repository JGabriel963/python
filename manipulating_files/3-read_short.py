stacks = []

with open("names.txt", "r") as file:
    for line in file:
        stacks.append(line.strip())

with open("names_asc.txt", "a") as file:
    for line in sorted(stacks):
        file.write(f"{line.strip()}\n")
