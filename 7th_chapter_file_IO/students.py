#with open("students.csv") as file:
#    for line in file:
#        name, house = line.rstrip().split(", ")
#        print(f"{name} from {house}")


# print in order 

#students = []
#
#with open ("students.csv") as file: 
#    for line in file:
#        name, house = line.rstrip() .split(", ")
#        student= {"name": name, "house": house}
#
#        #student["name"] = name
#        #student["house"] = house
#        students.append(student)
#
#
#def get_name (studnet):
#    return student["name"]
#
#
#
#
#for student in sorted(students, key= get_name):
#    print(f"{student['name']} from {student['house']}")


#useing lamda instant of calling a function for once. 


students =[]
with open ("students.csv") as file: 
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']}, from {student['house']}")