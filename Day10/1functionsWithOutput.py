# function with output - return value
# def my_function():
#     result = 3*4
#     return result

# output = my_function()

def format_name(firstName,lastName):
    if firstName == "" or lastName == "":
        return
    fname = firstName.title()
    lname = lastName.title()
    return fname + " " + lname

print(format_name("SaHil", "otari"))
