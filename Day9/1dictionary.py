# dictionary
# like table
# key and value pair

programming_dictionary = {
    "Bug": "An error in a program which prevents the program from running as expected.",
    "Function": "A piece of code that you can easuly call over and over again.",
    "Loop": "The actuon of doing something over and over again.",
}

# list[index]
# dictionary[key]
# print(programming_dictionary["Bug"])

# adding in dictionary
programming_dictionary["Variable"] = "Name of the memory address"
# print(programming_dictionary)


# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)


# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
