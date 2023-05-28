class User:
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f"Hello my name is {self.name}!")

lorraine = User("Lorraine")
rain = User("Rain")
lorraine.greeting()
rain.greeting()