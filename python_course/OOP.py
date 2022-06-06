class User:
    def __init__(self, username="default"):
        self.username = username
        self.follower = 0
        print(f"new user being created... : {username}")
    def follow(self):
        self.follower += 1
        print("new follow")

user_1 = User("username")
print(user_1.follower)
user_1.follow()
print(user_1.follower)