# class User:
#     def __init__(self) :
#         self.first_name = "Ada"
#         self.last_name = "Lovelace"
#         self.age = 42

# print("Hello!")

# user_ada = User()
# print(user_ada.first_name)

# user_2 = User()
# print(user_2.first_name)

# class User:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
    
#     def greeting(self):
#         print(f"hello my name is {self.first_name}!")

# Matthew = User("Matthew","B",24)
# cool_person = User("Hanna", "B", 24)
# Matthew.greeting()
# cool_person.greeting()


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0 

    def disply_info(self):
        print("{self.first_name}")
        print("{self.last_name}")
        print("{self.email}")
        print("{self.age}")

    def enroll(self):
        print(f"would you like to enroll {self.first_name}?")

    # def spend_points(self, amount):

Matthew = User("Matt", "B", "gmail", 22)

Matthew.disply_info()
Matthew.enroll()
# Matthew.spend_points()