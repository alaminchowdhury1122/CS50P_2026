# what is validate?

# It was a fucking day with out electricity

#email = input("what's your emaili? ") .strip()
#
#if "@" in email and "." in email:
#    print ("valid")
#
#else:
#    print("Invalid")

#email = input("what's your name? ").strip()
#
#username, domain = email.split("@")
#
#
#if username and "." in domain:
#    print("Valid")
#
#else:
#    print("Invalid")


# starting the day with re. 

import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")