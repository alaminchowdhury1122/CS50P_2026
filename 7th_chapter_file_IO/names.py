#names = []
#
#for _ in range (3):
#    names.append(input("what's your name ? "))
#
#
#for name in sorted(names):
#    print(f"hello, {name}")


#take input and store the name 
    
#name = input("what's your name? ")

#with open("store_name.txt", "a") as file:
#    file.write(f"{name}\n")


# read the existing file 

#with open ("store_name.txt", "r") as file:
#    lines = file.readlines()
#
#
#for i in lines:
#    print("hello,", i)

# better version to read existing text


#with open("store_name.txt", "r") as file:
#    for line in file:
#        print("hello", line.rstrip())
#

name = []

with open ("store_name.txt") as file: 
    for line in file:
        name.append(line.rstrip())


for i in sorted(name):
    print(f"hello, {i}")