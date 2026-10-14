name = input("what's your name ? ")

match name : 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    
    case "draco":
        print("slytherin")

    case _:
        print("Who")

# there's a lot of way to code in python
# you can shlove a problem in many ways