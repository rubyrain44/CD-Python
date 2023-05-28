class User:
    users = []

    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        User.users.append(self)

# Have this method print all of the users' details on separate lines.
    def display_info(self):
        print(f"User: {self.first_name} {self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}")    

# Have this method change the user's member status to True and set their gold card points to 200.
    def enroll(self, amount):
        self.is_rewards_member = True
        self.gold_card_points = amount

# Have this method decrease the user's points by the amount specified.
    def spend_points(self, amount):
        self.gold_card_points -= amount


Lorraine = User("Lorraine", "DAmore", "rain@mail.com", 34)
Rob = User("Rob", "Bear", "rob@mail.com", 33)
Gray = User("Gray", "Den", "gray@mail.com", 29)

Lorraine.display_info().spend_points(50)
Rob.enroll(200).spend_points(80)
users.display_info()
