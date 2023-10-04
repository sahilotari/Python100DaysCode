# class is a blueprint
# first letter of every word should be capitalized- PascalCase


class User:
    def __init__(self, user_id, username):
        # print("new user being created....")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Sahil")
user_2 = User("002", "Om")
user_1.follow(user_2)
print(
    f"ID: {user_1.id}, Username:  {user_1.username}, followers: {user_1.followers}, following: {user_1.following}"
)
print(
    f"ID: {user_2.id}, Username:  {user_2.username}, followers: {user_2.followers}, following: {user_2.following}"
)
