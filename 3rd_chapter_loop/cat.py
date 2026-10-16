#i = 0
#while i < 3:
#   print("meow")
#    i = i +1

#for _ in range(3):
#    print("I'm great")

#print("meow\n" * 3, end="")


#while True:
#    n = int(input("what's n ?"))
#    if n > 0:
#        break

#for _ in range(n):
#    print("meow")


# useing own function 

def main(): 
    number = get_number()
    meow(number)

def get_number ():
    while True:
        n = int(input("what's n? "))
        if n > 0 :
            break
    return n


def meow (n):
    for _ in range(n):
        print("meow")
main()