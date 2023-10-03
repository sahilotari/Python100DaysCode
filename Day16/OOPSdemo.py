# import turtle

# # creating objects
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")

# # object attributes
# my_screen = turtle.Screen()
# print(my_screen.canvheight)


# # object methods
# my_screen.exitonclick()


# use external packages
# install them using pip : python -m pip install prettytable
# use them

import prettytable

table = prettytable.PrettyTable()
# print(table)
table.align = "l"
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
