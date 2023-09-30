def format_name(firstName,lastName):
    """Take a first and last name and format it to return title case version"""
    if firstName == "" or lastName == "":
        return
    fname = firstName.title()
    lname = lastName.title()
    return fname + " " + lname

print(format_name("SaHil", "otari"))\

# Docstring - While using the function in program
# it shows this docstring which can be helpful for 
# programmer to understand its use or purpose.