# global scope
enemies = 1


def increase_enemies():
    enemies = 2  # local scope
    print(f"Enemies inside function: {enemies}")


increase_enemies()

print(f"Enemies outside function: {enemies}")


# there is no Block Scope

enemies = ["Skeleton","Zombie"]
game_level = 3
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
# Even though new_enemy is in block of 'if', it is accessible out of 'if' block.