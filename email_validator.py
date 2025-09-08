#Simple bascic email slicer

# email = input("Enter your email: ")
# index = email.index("@")
# username = email[:index] # or  username = email[:email.index("@")]
# domain = email[index + 1:] # domain = email[email.index("@") + 1:]
# print(f"Your username is {username} and domain is {domain}")

#Email Validator

email = input("Enter your email: ")

if "@" in email and "." in email and " " not in email:
    at_index = email.index("@")
    dot_index = email.rfind(".")
    
    if at_index > 0 and dot_index > at_index + 1 and dot_index < len(email)-1:
        username = email[: at_index]
        domain = email[at_index + 1 : dot_index]
        extension = email[dot_index + 1:]
        
        print("Valid email")
        print(f"Username: {username}")
        print(f"Domain: {domain}")
        print(f"Extension: {extension}")
    else:
        print("Invalid Email (wrong placement of @ or .)")
    
else:
    print("Invalid Email(missing @ , . or contains space)")