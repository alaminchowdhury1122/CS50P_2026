name = input("what's your name ? ")

match name : 
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    
    case "draco":
        print("slytherin")

    case _:
        print("Who")