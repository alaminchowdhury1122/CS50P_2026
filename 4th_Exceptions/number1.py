def main():
    x= get_int("What's X? ")
    print(f"x is {x}")

def get_int(prompt):

    while True: 
        try:
            x = int(input(prompt))

        except ValueError:
            print("X is not an interger")

        else:
           return x 


main()