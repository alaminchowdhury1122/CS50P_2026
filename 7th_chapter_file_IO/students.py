#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(", ")
#        print(f"{name} from {house}")


# print in order 

students = []

with open ("students.csv") as file: 
    for line in file:
        name, house = line.rstrip() .split(", ")
        students.append(f"{name} from {house}")


for student in sorted (students):
    print(student)